package parsinglogfiles

import (
	"fmt"
	"regexp"
	"strings"
)

func IsValidLine(text string) bool {
	logLevels := []string{"[TRC]", "[DBG]", "[INF]", "[WRN]", "[ERR]", "[FTL]"}
	if len(text) < 5 {
		return false
	}
	for _, levels := range logLevels {
		if levels == text[:5] {
			return true
		}
	}
	return false
}

func SplitLogLine(text string) []string {
	re := regexp.MustCompile("<[-=$*~]*>")
	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	re := regexp.MustCompile("\".*password\"")
	count := 0
	for _, line := range lines {
		if re.Match([]byte(strings.ToLower(line))) {
			count++
		}
	}
	return count
}

func RemoveEndOfLineText(text string) string {
	re := regexp.MustCompile("end-of-line\\d*")
	return string(re.ReplaceAll([]byte(text), []byte("")))
}

func TagWithUserName(lines []string) []string {
	re := regexp.MustCompile(`(?:User)\s+(\w*)`)
	var newLines []string
	for _, line := range lines {
		if re.MatchString(line) {
			userName := re.FindStringSubmatch(line)
			tag := "[USR]"
			newLines = append(
				newLines,
				fmt.Sprintf("%s %s %s", tag, userName[1], line),
			)
		} else {
			newLines = append(newLines, line)
		}
	}
	return newLines
}
