package main

import (
	"github.com/joho/godotenv"
	"github.com/simonnordberg/aoc/cmd"
)

func main() {
	// Load .env file if it exists (silently continues if not found)
	_ = godotenv.Load()

	cmd.Execute()
}
