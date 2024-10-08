package atbash

import (
	"strings"
)

func genEvalMap() map[string]string {
	evalMap := map[string]string{}
	startKey := 97 
	for startValue := 122; startValue >= 97; startValue-- {
		evalMap[string(rune(startKey))] = string(rune(startValue))
		startKey++
	}
	return evalMap
}

func onlyLetters(s string) string {
	var newString strings.Builder
	for _, letter := range s {
		if letter >= 97 && letter <= 122 || letter >= 48 && letter <= 57 {
			newString.WriteRune(letter)
		}
	}
	return newString.String()
}

func replaceLetters(l string) string {
	evalMap := genEvalMap()
	var newString strings.Builder
	for _, letter := range l {
		eval := evalMap[string(letter)]
		if eval == "" {
			eval = string(letter)
		}
		newString.WriteString(eval)
	}
	return newString.String()
}

func Atbash(s string) string {
	newString := onlyLetters(strings.ToLower(s))
	replaced := replaceLetters(newString)
	var gt strings.Builder

	for i, letter := range replaced {
		if i%5 == 0 && i != 0 {
			gt.WriteRune(' ')
		}
		gt.WriteRune(letter)
	}
	return gt.String()
}
