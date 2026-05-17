package main

import (
	"fmt"
	"strings"
)

func Reverse(word string) string {
	var newWord strings.Builder

	for i := len(word) - 1; i >= 0; i-- {
		newWord.WriteByte(word[i])
	}

	return newWord.String()
}

func ReverseWords(str string) string {
	var newWord strings.Builder

	lastIdx := 0
	for idx, char := range str {
		if idx == len(str)-1 {
			newWord.WriteString(Reverse(str[lastIdx : idx+1]))
		}
		if char == ' ' {
			newWord.WriteString(Reverse(str[lastIdx:idx]))
			newWord.WriteRune(char)
			lastIdx = idx + 1
		}
	}

	return newWord.String()
}

func main() {
	fmt.Println(ReverseWords("This is an example!"))
	fmt.Println(ReverseWords("double  spaces"))
}
