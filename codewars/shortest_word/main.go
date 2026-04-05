package main

import (
	"fmt"
	"strings"
)

func FindShort(s string) int {
	words := strings.Split(s, " ")

	shortest := len(words[0])

	for _, word := range words[1:] {
		if size := len(word); size < shortest {
			shortest = size
		}
	}

	return shortest

}

func main() {
	fmt.Println(FindShort("bitcoin take over the world maybe who knows perhaps"))
}
