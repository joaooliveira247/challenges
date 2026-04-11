package main

import (
	"fmt"
	"strings"
)

func ReverseLetters(s string) string {
	var newString strings.Builder

	for i := len(s) - 1; i >= 0; i-- {
		if letter := rune(s[i]); letter > 64 && letter < 91 || letter > 96 && letter < 123 {
			newString.WriteRune(letter)
		}
	}

	return newString.String()
}

func main() {
	fmt.Println(ReverseLetters("krishan"))
	fmt.Println(ReverseLetters("ultr53o?n"))
}
