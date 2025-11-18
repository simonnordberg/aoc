package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "aoc",
	Short: "Advent of Code helper",
	Long: `A CLI tool to help with Advent of Code challenges.
Fetch puzzle inputs and run daily solutions.`,
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	rootCmd.AddCommand(fetchCmd)
	rootCmd.AddCommand(runCmd)
}


