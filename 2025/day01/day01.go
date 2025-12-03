package day01

import (
	"aoc2025/util"
	"fmt"
	"strconv"
)

func Solve() {
	lines := util.ReadLines("day01/input.txt")

	zeroHitCount := 0
	zeroPassCount := 0
	currentStep := 50

	for _, line := range lines {
		direction, steps := parseLine(line)
		newStep, zeroPasses := move(currentStep, direction, steps)
		currentStep = newStep
		zeroPassCount += zeroPasses
		if currentStep == 0 {
			zeroHitCount++
		}
	}

	fmt.Printf("Part 1: %d\n", zeroHitCount)
	fmt.Printf("Part 2: %d\n", zeroPassCount)
}

func parseLine(line string) (direction int, steps int) {
	if line[0] == 'L' {
		direction = -1
	} else {
		direction = 1
	}
	steps, _ = strconv.Atoi(line[1:])
	return direction, steps
}

func move(currentStep int, direction int, steps int) (newStep int, zeroPasses int) {
	for steps > 0 {
		steps--
		currentStep += direction

		if currentStep == 100 {
			currentStep = 0
		}
		if currentStep == -1 {
			currentStep = 99
		}
		if currentStep == 0 {
			zeroPasses++
		}
	}
	return currentStep, zeroPasses
}
