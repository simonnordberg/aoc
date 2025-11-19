package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var (
	runYear int
)

var runCmd = &cobra.Command{
	Use:   "run <day>",
	Short: "Run the solution for a specific day",
	Long: `Run the Advent of Code solution for a specific day.

Example: aoc run 1 --year 2024`,
	Args: cobra.ExactArgs(1),
	RunE: runRun,
}

func init() {
	runCmd.Flags().IntVarP(&runYear, "year", "y", getCurrentYear(), "Year of the puzzle")
}

func runRun(cmd *cobra.Command, args []string) error {
	var day int
	_, err := fmt.Sscanf(args[0], "%d", &day)
	if err != nil {
		return fmt.Errorf("invalid day format: %w", err)
	}

	if day < 1 || day > 25 {
		return fmt.Errorf("day must be between 1 and 25, got %d", day)
	}

	// TODO: Implement running the solution
	fmt.Printf("Running solution for %d day %d\n", runYear, day)
	return nil
}
