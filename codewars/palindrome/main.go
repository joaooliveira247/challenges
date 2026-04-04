package main

import (
	"fmt"
	"strings"
)

func IsPalindrome(str string) bool {
	str = strings.ToLower(str)
	var reversedString strings.Builder

	for i := len(str) - 1; i >= 0; i-- {
		reversedString.WriteByte(str[i])
	}

	return str == reversedString.String()
}

func main() {
	fmt.Println(IsPalindrome("mom"))
	fmt.Println(IsPalindrome("a"))
	fmt.Println(IsPalindrome("Abba"))
	fmt.Println(IsPalindrome("house"))
}
