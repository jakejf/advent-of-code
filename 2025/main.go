package main

import (
	"aoc2025/day01"
	"aoc2025/day02"
	"os"
)

func main() {
	day := os.Args[1]
	switch day {
	case "1":
		day01.Solve()
	case "2":
		day02.Solve()
	default:
		println("Day not implemented")
	}
}
