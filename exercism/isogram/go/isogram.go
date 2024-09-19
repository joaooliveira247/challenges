package isogram

import "strings"

func IsIsogram(word string) bool {
	counter := map[string]int{}
	for _, letter := range strings.ToLower(word) {
		counter[string(letter)]++
	}

	delete(counter, " ")
	delete(counter, "-")
	for _, total := range counter {
		if total > 1 {
			return false
		}
	}
	return true
}
