package main

import (
	"fmt"
	"strings"
)

func reverseString(s string) string {
	switch size := len(s); size {
	case 1:
		return s
	case 2:
		return string(s[1]) + string(s[0])
	default:
		return string(s[size-1]) + s[1:size-1] + string(s[0])
	}
}

func EncryptThis(text string) string {
	if len(text) == 0 {
		return text
	}

	words := strings.Split(text, " ")

	for idx, word := range words {
		if len(word) < 2 {
			words[idx] = fmt.Sprintf("%d", word[0])
			continue
		}
		words[idx] = fmt.Sprintf("%d%s", word[0], reverseString(word[1:]))
	}

	return strings.Join(words, " ")
}

func main() {
	fmt.Println(EncryptThis("hello world"))
	fmt.Println(EncryptThis("A wise old owl lived in an oak"))
}
