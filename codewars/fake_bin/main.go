package main

import (
	"fmt"
	"strings"
)

func FakeBin(x string) string {
	var newString strings.Builder

	for _, char := range x {
		if (char - 48) < 5 {
			newString.WriteString("0")
			continue
		}
		newString.WriteString("1")
	}
	return newString.String()
}

func main() {
	fmt.Println(FakeBin("45385593107843568"))
}
