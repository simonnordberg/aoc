package solutions

import (
	"fmt"
)

type Solver interface {
	Part1(input string) (string, error)
	Part2(input string) (string, error)
}

var Registry = make(map[int]map[int]Solver)

func Register(year, day int, solver Solver) {
	if Registry[year] == nil {
		Registry[year] = make(map[int]Solver)
	}
	Registry[year][day] = solver
}

func Get(year, day int) (Solver, error) {
	if Registry[year] == nil {
		return nil, fmt.Errorf("no solutions registered for year %d", year)
	}
	solver, ok := Registry[year][day]
	if !ok {
		return nil, fmt.Errorf("no solution registered for year %d day %d", year, day)
	}
	return solver, nil
}

