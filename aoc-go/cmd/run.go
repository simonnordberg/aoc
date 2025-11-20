package cmd

import (
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"

	"github.com/simonnordberg/aoc/solutions"
	_ "github.com/simonnordberg/aoc/solutions/y2024"
)

var runYear int

var runCmd = &cobra.Command{
	Use:   "run <day> <part>",
	Short: "Run the solution for a specific day",
	Long: `Run the Advent of Code solution for a specific day.

Input is read from stdin. Day must be 1-25, part must be 1-2.

Example: cat input.txt | aoc run 1 1
         cat input.txt | aoc run 5 2 --year 2023`,
	Args: cobra.ExactArgs(2),
	RunE: runRun,
}

func init() {
	runCmd.Flags().IntVarP(&runYear, "year", "y", getCurrentYear(), "Year of the puzzle")
}

func runRun(cmd *cobra.Command, args []string) error {
	var day, part int
	_, err := fmt.Sscanf(args[0], "%d", &day)
	if err != nil {
		return fmt.Errorf("invalid day format: %w", err)
	}
	_, err = fmt.Sscanf(args[1], "%d", &part)
	if err != nil {
		return fmt.Errorf("invalid part format: %w", err)
	}

	if day < 1 || day > 25 {
		return fmt.Errorf("day must be between 1 and 25, got %d", day)
	}
	if part < 1 || part > 2 {
		return fmt.Errorf("part must be 1 or 2, got %d", part)
	}

	// Get the solver from the registry
	solver, err := solutions.Get(runYear, day)
	if err != nil {
		return err
	}

	// Read input from stdin
	input, err := io.ReadAll(os.Stdin)
	if err != nil {
		return fmt.Errorf("failed to read from stdin: %w", err)
	}

	// Run the specified part
	if part == 1 {
		result, err := solver.Part1(string(input))
		if err != nil {
			return fmt.Errorf("part 1 failed: %w", err)
		}
		fmt.Println(result)
	} else {
		result, err := solver.Part2(string(input))
		if err != nil {
			return fmt.Errorf("part 2 failed: %w", err)
		}
		fmt.Println(result)
	}

	return nil
}
