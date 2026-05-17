package util

import (
	"os"
	"strings"
)

func ReadLines(path string) []string {
	data, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	normalized := strings.ReplaceAll(string(data), "\r\n", "\n")
	return strings.Split(strings.TrimSpace(normalized), "\n")
}
