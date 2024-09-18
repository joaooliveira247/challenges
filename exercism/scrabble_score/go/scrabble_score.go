package scrabble

import "strings"

func letterFilter(letterEvalution map[int][]string, value string) int {
	for evaluation, letters := range letterEvalution {
		for _, letter := range letters {
			if letter == strings.ToUpper(value) {
				return evaluation
			}
		}
	}
	return 0
}

func Score(word string) int {
	letterEvaluation := map[int][]string{
		1:  {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"},
		2:  {"D", "G"},
		3:  {"B", "C", "M", "P"},
		4:  {"F", "H", "V", "W", "Y"},
		5:  {"K"},
		8:  {"J", "X"},
		10: {"Q", "Z"},
	}

	if word == "" {
		return 0
	}

	var total int
	for _, letter := range word {
		total += letterFilter(letterEvaluation, string(letter))
	}
	return total
}
