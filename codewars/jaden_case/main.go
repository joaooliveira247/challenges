package main

import (
	"fmt"
	"strings"
)

func Totile(str string) string {
	if firstChar := rune(str[0]); firstChar > 96 && firstChar < 123 {
		return string(firstChar-32) + str[1:]
	}
	return str
}

func ToJadenCase(str string) string {
	words := strings.Split(str, " ")

	for i, word := range words {
		words[i] = Totile(word)
	}

	return strings.Join(words, " ")
}

func main() {
	fmt.Println(ToJadenCase("How can mirrors be real if our eyes aren't real"))
}
