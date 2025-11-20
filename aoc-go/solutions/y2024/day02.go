package y2024

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/simonnordberg/aoc/solutions"
)

type day02 struct{}

func init() {
	solutions.Register(2024, 2, day02{})
}

func testSign(diffs []int) bool {
	if len(diffs) == 0 {
		return true
	}
	allPositive := true
	allNegative := true
	for _, d := range diffs {
		if d <= 0 {
			allPositive = false
		}
		if d >= 0 {
			allNegative = false
		}
	}
	return allPositive || allNegative
}

func testDist(diffs []int) bool {
	for _, d := range diffs {
		abs := d
		if abs < 0 {
			abs = -abs
		}
		if abs < 1 || abs > 3 {
			return false
		}
	}
	return true
}

func test(levels []int, dampener bool) bool {
	if dampener {
		// Try removing each level
		for i := 0; i < len(levels); i++ {
			// Create slice without element at index i
			reduced := append([]int{}, levels[:i]...)
			reduced = append(reduced, levels[i+1:]...)
			if test(reduced, false) {
				return true
			}
		}
		return false
	}

	// Calculate differences
	if len(levels) < 2 {
		return true
	}

	diffs := make([]int, len(levels)-1)
	for i := 0; i < len(levels)-1; i++ {
		diffs[i] = levels[i] - levels[i+1]
	}

	return testSign(diffs) && testDist(diffs)
}

func (day02) Part1(input string) (string, error) {
	lines := strings.Split(strings.TrimSpace(input), "\n")

	count := 0
	for _, line := range lines {
		if line == "" {
			continue
		}

		parts := strings.Fields(line)
		levels := make([]int, len(parts))
		for i, part := range parts {
			level, err := strconv.Atoi(part)
			if err != nil {
				return "", err
			}
			levels[i] = level
		}

		if test(levels, false) {
			count++
		}
	}

	return fmt.Sprintf("%d", count), nil
}

func (day02) Part2(input string) (string, error) {
	lines := strings.Split(strings.TrimSpace(input), "\n")

	count := 0
	for _, line := range lines {
		if line == "" {
			continue
		}

		parts := strings.Fields(line)
		levels := make([]int, len(parts))
		for i, part := range parts {
			level, err := strconv.Atoi(part)
			if err != nil {
				return "", err
			}
			levels[i] = level
		}

		if test(levels, true) {
			count++
		}
	}

	return fmt.Sprintf("%d", count), nil
}

