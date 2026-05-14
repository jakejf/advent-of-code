package day02

import (
	"aoc2025/util"
	"fmt"
	"strconv"
	"strings"
)

func Solve() {
	lines := util.ReadLines("day02/input.txt")

	ranges := strings.Split(lines[0], ",")

	var sumInvalidPartOne int
	var sumInvalidPartTwo int

	for _, r := range ranges {
		bounds := strings.Split(r, "-")
		start, _ := strconv.Atoi(bounds[0])
		end, _ := strconv.Atoi(bounds[1])

		for i := start; i <= end; i++ {
			if isInvalidPartOne(strconv.Itoa(i)) {
				sumInvalidPartOne += i
			}
			if isInvalidPartTwo(strconv.Itoa(i)) {
				sumInvalidPartTwo += i
			}
		}
	}

	fmt.Printf("Part 1: %d\n", sumInvalidPartOne)
	fmt.Printf("Part 2: %d\n", sumInvalidPartTwo)
}

func isInvalidPartOne(id string) bool {
	if len(id)%2 != 0 {
		return false
	}

	left := id[:len(id)/2]
	right := id[len(id)/2:]

	return left == right
}

func isInvalidPartTwo(id string) bool {
	i := id + id
	return strings.Contains(i[1:len(i)-1], id)
}
