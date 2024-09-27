// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package bob should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package bob

import (
	"strings"
	"unicode"
)

func cleanString(s string) string {
	var builder strings.Builder
	for _, letter := range s {
		if unicode.IsLetter(letter) {
			builder.WriteRune(letter)
		}
	}
	return builder.String()
}

func isAllUpper(s string) bool {
	newString := cleanString(s)

	if len(newString) < 1 {
		return false
	}

	for _, letter := range newString {
		if (letter >= 97 && letter <= 122) || letter == 32 {
			return false
		}
	}
	return true
}

func isQuestion(s string) bool {
	if len(s) < 1 {
		return false
	}
	return s[len(s)-1] == 63
}

// Hey should have a comment documenting it.
func Hey(remark string) string {
	/*
		Sure - end with ?
		"Whoa, chill out!" - all uppercase
		"Calm down, I know what I'm doing!" - end with ? and all uppercase
		"Fine. Be that way!"  -white space or nil
		"Whatever." - anything else
	*/
	switch {
	case isAllUpper(remark) && strings.Contains(remark, "?"):
		return "Calm down, I know what I'm doing!"
	case isAllUpper(remark):
		return "Whoa, chill out!"
	case isQuestion(strings.ReplaceAll(remark, " ", "")):
		return "Sure."
	case len(strings.TrimSpace(remark)) < 1:
		return "Fine. Be that way!"
	default:
		return "Whatever."

	}
}
