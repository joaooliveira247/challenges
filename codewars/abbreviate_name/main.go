package main

import (
	"fmt"
	"strings"
)

func AbbrevName(name string) string {
	names := strings.Split(name, " ")

	for idx, word := range names {
		names[idx] = strings.ToUpper(string(word[0]))
	}

	return strings.Join(names, ".")
}

func main() {
	fmt.Println(AbbrevName("Elon Musk"))
}
