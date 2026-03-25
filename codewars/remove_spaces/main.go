package main

import (
	"fmt"
	"strings"
)

func NoSpace(word string) string {
	var newString strings.Builder

	for _, char := range word {
		if char != ' ' {
			newString.WriteRune(char)
		}
	}

	return newString.String()
}

func main() {
	examples := []string{
		"8 j 8   mBliB8g  imjB8B8  jl  B",
		"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd",
		"8aaaaa dddd r     ",
	}

	for _, example := range examples {
		fmt.Printf("%s -> %s\n", example, NoSpace(example))
	}
}
