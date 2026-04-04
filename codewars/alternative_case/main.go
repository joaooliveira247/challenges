package main

import (
	"fmt"
	"strings"
)

func letterSwap(char rune) rune {
	if char > 96 && char < 123 {
		return char - 32
	} else if char > 64 && char < 91 {
		return char + 32
	}
	return char
}

func ToAlternatingCase(str string) string {
	var newString strings.Builder

	for _, char := range str {
		newString.WriteRune(letterSwap(char))
	}
	return newString.String()
}

func main() {
	fmt.Println(ToAlternatingCase("Hello World"))
}
