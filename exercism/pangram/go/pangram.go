package pangram

import "strings"

func IsPangram(input string) bool {
	chars := map[rune]int{}
	for _, char := range []rune(strings.ToLower(input)) {
		if char > 96 && char < 123 {
			chars[char]++
		}
	}
	if len(chars) == 26 {
		return true
	}
	return false
}
