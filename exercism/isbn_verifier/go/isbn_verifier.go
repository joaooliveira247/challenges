package isbn

import (
	"slices"
	"strconv"
	"unicode"
)

func IsValidISBN(isbn string) bool {
	codes := []int{}

	for _, value := range isbn {
		if value > 48 && value < 58 {
			num, _ := strconv.Atoi(string(value))
			codes = append(codes, num)
		}
		if value == 'X' {
			codes = append(codes, 10)
		}
		if unicode.IsLetter(value) && value != 'X' {
			return false
		}
	}

	if length := len(codes); length < 9 || length > 10 {
		return false
	}

	slices.Reverse(codes)

	total := 0

	for i := 0; i < len(codes); i++ {
		total += codes[i] * (i + 1)
	}
	return total%11 == 0

}
