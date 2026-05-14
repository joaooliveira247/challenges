package main

import (
	"fmt"
	"strings"
)

func Format(name string, number int) string {
	var numeral strings.Builder

	switch {
	case number%10 == 1 && number%100 != 11:
		numeral.WriteString(fmt.Sprintf("%dst", number))
	case number%10 == 2 && number%100 != 12:
		numeral.WriteString(fmt.Sprintf("%dnd", number))
	case number%10 == 3 && number%100 != 13:
		numeral.WriteString(fmt.Sprintf("%drd", number))
	default:
		numeral.WriteString(fmt.Sprintf("%dth", number))
	}

	return fmt.Sprintf("%s, you are the %s customer we serve today. Thank you!", name, numeral.String())
}

func main() {
	fmt.Println(Format("Mary", 1))
	fmt.Println(Format("John", 12))
	fmt.Println(Format("Dahir", 163))
	fmt.Println(Format("Michael", 1987))
}
