package main

import (
	"fmt"
	"strings"
)

func onlyLetters(s string) string {
	var newString strings.Builder
	
	for _, char := range s {
		if char >= 'a' && char <= 'z' || char >= 'A' && char <= 'Z' {
			newString.WriteRune(char)
		}
	}
	return newString.String()
}

func Abbreviate(s string) string {
	removeDashWords := strings.ReplaceAll(s, "-", " ")
	words := strings.Split(removeDashWords, " ")

	var acronym strings.Builder

	for _, word := range words {
		if word != "" {
			acronym.WriteString(strings.ToUpper(string(onlyLetters(word)[0])))
		}
	}

	return acronym.String()

}

func main() {
	fmt.Println(Abbreviate("As Soon As Possible"))
	fmt.Println(Abbreviate("Liquid-crystal display"))
	fmt.Println(Abbreviate("Thank George It's Friday!"))
	fmt.Println(Abbreviate("Something - I made up from thin air"))
	fmt.Println(Abbreviate("The Road _Not_ Taken"))
}
