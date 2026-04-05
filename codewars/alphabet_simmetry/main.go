package main

import (
	"fmt"
	"strings"
)

func evalueteLetter(char rune) rune {
	return char - 96
}

func letterPosition(s string) int {
	s = strings.ToLower(s)

	var counter int

	for idx, letter := range s {
		if idx+1 == int(evalueteLetter(letter)) {
			counter++
		}
	}

	return counter
}

func solve(slice []string) []int {
	var result []int

	for _, str := range slice {
		result = append(result, letterPosition(str))
	}
	return result
}

func main() {
	fmt.Println(solve([]string{"abode", "ABc", "xyzD"}))
	// fmt.Println(greatestIdx("abode"))
}
