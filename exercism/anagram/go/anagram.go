package anagram

import (
	"slices"
	"strings"
)

func hasSameLetters(target []rune, word []rune) bool {
	if len(target) != len(word) {
		return false
	}
	slices.Sort(target)
	slices.Sort(word)
	for i, letter := range target {
		if letter != word[i] {
			return false
		}
	}
	return true
}

func Detect(subject string, candidates []string) []string {
	valids := []string{}

	for _, candidate := range candidates {
		lowerSubject := strings.ToLower(subject)
		lowerCandidate := strings.ToLower(candidate)
		if lowerCandidate == lowerSubject {
			continue
		}
		if hasSameLetters(
			[]rune(lowerSubject),
			[]rune(lowerCandidate),
		) {
			valids = append(valids, candidate)
		}
	}
	return valids
}
