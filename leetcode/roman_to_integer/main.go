package main

import (
	"fmt"
	"strings"
)

func romanToInt(s string) int {
	var num int
	variations := map[string]int{
		"IV": 4,
		"IX": 9,
		"XL": 40,
		"XC": 90,
		"CD": 400,
		"CM": 900,
	}

	for variation, val := range variations {
		if strings.Contains(s, variation) {
			s = strings.ReplaceAll(s, variation, "")
			num += val
		}
	}

	eval := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	for _, letter := range s {
		num += eval[letter]
	}

	return num
}

func main() {
	num := "MCMXCIV"
	fmt.Println(romanToInt(num))
}
