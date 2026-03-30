package main

import (
	"fmt"
	"strings"
)

func MakeUpperCase(str string) string {
	var newString strings.Builder

	for _, char := range str {
		if char > 96 && char < 123 {
			newString.WriteRune(char - 32)
			continue
		}
		newString.WriteRune(char)
	}

	return newString.String()
}

func main() {
	fmt.Println(MakeUpperCase("heLlO wORLd !"))
	fmt.Println(MakeUpperCase("2HLQaOMUO6"))
}
