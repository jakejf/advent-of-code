package day03

import (
	"aoc2025/util"
	"fmt"
	"math"
)

func Solve() {
	banks := util.ReadLines("day03/input.txt")

	// Part 1
	var total int
	for _, bank := range banks {
		firstIndex, firstValue := findHighest(bank[:len(bank)-2])
		_, secondValue := findHighest(bank[firstIndex+1 : len(bank)-1])
		total += firstValue*10 + secondValue
	}
	fmt.Printf("Part 1: %d\n", total)

	// Part 2
	total = 0
	for _, bank := range banks {
		var currentMax int
		var currentIndex int
		for i := range 12 {
			index, digit := findHighest(bank[currentIndex : len(bank)-11+i])
			currentMax += digit * int(math.Pow10(11-i))
			currentIndex += index + 1
		}
		total += currentMax
	}
	fmt.Printf("Part 2: %d\n", total)
}

func findHighest(s string) (index int, value int) {
	index = 0
	value = int(s[0] - '0')

	for i := 1; i < len(s); i++ {
		curr := int(s[i] - '0')
		if curr > value {
			index = i
			value = curr
		}
	}
	return index, value
}
