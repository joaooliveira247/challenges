package logs

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

// Application identifies the application emitting the given log.
func Application(log string) string {
	unicodeTable := map[string]string{
		"U+2757":  "recommendation",
		"U+1F50D": "search",
		"U+2600":  "weather",
	}
	var chars []string
	for _, char := range log {
		if code := fmt.Sprintf("%U", char); unicodeTable[code] != "" {
			chars = append(chars, code)
		}
	}
	if len(chars) == 0 {
		return "default"
	}
	return unicodeTable[chars[0]]
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {
	return strings.ReplaceAll(log, string(oldRune), string(newRune))
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	return utf8.RuneCountInString(log) <= limit
}
