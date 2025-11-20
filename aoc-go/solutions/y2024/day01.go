package y2024

import (
	"fmt"
	"sort"
	"strconv"
	"strings"

	"github.com/simonnordberg/aoc/solutions"
)

type day01 struct{}

func init() {
	solutions.Register(2024, 1, day01{})
}

func (day01) Part1(input string) (string, error) {
	lines := strings.Split(strings.TrimSpace(input), "\n")

	var left, right []int
	for _, line := range lines {
		parts := strings.Fields(line)
		if len(parts) < 2 {
			continue
		}

		l, err := strconv.Atoi(parts[0])
		if err != nil {
			return "", err
		}
		r, err := strconv.Atoi(parts[1])
		if err != nil {
			return "", err
		}

		left = append(left, l)
		right = append(right, r)
	}

	sort.Ints(left)
	sort.Ints(right)

	totalDistance := 0
	for i := range left {
		diff := left[i] - right[i]
		if diff < 0 {
			diff = -diff
		}
		totalDistance += diff
	}

	return fmt.Sprintf("%d", totalDistance), nil
}

func (day01) Part2(input string) (string, error) {
	lines := strings.Split(strings.TrimSpace(input), "\n")

	var left []int
	rightCounts := make(map[int]int)

	for _, line := range lines {
		parts := strings.Fields(line)
		if len(parts) < 2 {
			continue
		}

		l, err := strconv.Atoi(parts[0])
		if err != nil {
			return "", err
		}
		r, err := strconv.Atoi(parts[1])
		if err != nil {
			return "", err
		}

		left = append(left, l)
		rightCounts[r]++
	}

	totalSimilarity := 0
	for _, num := range left {
		totalSimilarity += num * rightCounts[num]
	}

	return fmt.Sprintf("%d", totalSimilarity), nil
}

