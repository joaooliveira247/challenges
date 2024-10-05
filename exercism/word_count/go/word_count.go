package wordcount

import (
	"regexp"
	"strings"
)

type Frequency map[string]int

func WordCount(phrase string) Frequency {
	counter := Frequency{}
	re := regexp.MustCompile(`\b\w+(?:\'\w+)?\b`)
	for _, word := range re.FindAllString(strings.ToLower(phrase), -1) {
		counter[word]++
	}
	return counter
}
