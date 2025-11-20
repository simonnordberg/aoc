package cmd

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	"github.com/spf13/cobra"
)

var (
	fetchYear      int
	fetchDebug     bool
	fetchStdout    bool
	fetchInputName string
)

var fetchCmd = &cobra.Command{
	Use:   "fetch <day>",
	Short: "Fetch puzzle input for a specific day",
	Long: `Fetch the puzzle input from adventofcode.com for a specific day.
Requires AOC_SESSION environment variable to be set with your session cookie.

By default, saves to a file named 'input'. Use --input flag to override.

Example: aoc fetch 1 --year 2024
         aoc fetch 5 --input input2 --year 2024`,
	Args: cobra.ExactArgs(1),
	RunE: runFetch,
}

func init() {
	fetchCmd.SilenceUsage = true
	fetchCmd.Flags().IntVarP(&fetchYear, "year", "y", getCurrentYear(), "Year of the puzzle")
	fetchCmd.Flags().BoolVarP(&fetchDebug, "debug", "d", false, "Print fetched content to stdout")
	fetchCmd.Flags().BoolVar(&fetchStdout, "stdout", false, "Output to stdout instead of saving to file")
	fetchCmd.Flags().StringVar(&fetchInputName, "input", "input", "Filename of the input file to fetch and save with the same name (e.g., input, input2, input3)")
}

func runFetch(cmd *cobra.Command, args []string) error {
	var day int
	_, err := fmt.Sscanf(args[0], "%d", &day)
	if err != nil {
		return fmt.Errorf("invalid day format: %w", err)
	}

	if day < 1 || day > 25 {
		return fmt.Errorf("day must be between 1 and 25, got %d", day)
	}

	filename := fetchInputName

	// Get session cookie
	cookie := os.Getenv("AOC_SESSION")
	if cookie == "" {
		return fmt.Errorf("AOC_SESSION environment variable not set. Please set your session cookie")
	}

	// Fetch the input
	content, err := fetchInputContent(fetchYear, day, filename, cookie)
	if err != nil {
		return err
	}

	// Output to stdout if requested
	if fetchStdout {
		fmt.Print(content)
		return nil
	}

	// Create testdata directory path: testdata/YYYY/dayDD/
	testdataDir := filepath.Join("testdata", strconv.Itoa(fetchYear), fmt.Sprintf("day%02d", day))
	if err := os.MkdirAll(testdataDir, 0755); err != nil {
		return fmt.Errorf("failed to create testdata directory %s: %w", testdataDir, err)
	}

	// Write to file in testdata directory
	filePath := filepath.Join(testdataDir, filename)
	if err := writeToFile(content, filePath); err != nil {
		return err
	}

	if fetchDebug {
		fmt.Println(content)
	}

	fmt.Printf("✓ Puzzle input for %d day %d saved to %s\n", fetchYear, day, filePath)
	return nil
}

func fetchInputContent(year, day int, filename, cookie string) (string, error) {
	url := fmt.Sprintf("https://adventofcode.com/%d/day/%d/%s", year, day, filename)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "", fmt.Errorf("failed to create request: %w", err)
	}

	req.AddCookie(&http.Cookie{
		Name:  "session",
		Value: cookie,
	})

	client := &http.Client{
		Timeout: 10 * time.Second,
	}

	resp, err := client.Do(req)
	if err != nil {
		return "", fmt.Errorf("failed to fetch input: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return "", fmt.Errorf("unexpected status code %d: %s", resp.StatusCode, string(body))
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("failed to read response: %w", err)
	}

	return strings.TrimSpace(string(body)), nil
}

func writeToFile(content, filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("failed to create file: %w", err)
	}
	defer file.Close()

	_, err = file.WriteString(content)
	if err != nil {
		return fmt.Errorf("failed to write to file: %w", err)
	}

	return nil
}

func getCurrentYear() int {
	return time.Now().Year()
}
