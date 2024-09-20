package luhn

import (
	"slices"
	"strconv"
	"strings"
)

func isValidLength(id string) bool {
	validFormat := strings.Split(id, " ")
	if len(id) < 2 || len(validFormat) < 1 {
		return false
	}
	return true
}

func sumSlice(slice []int) int {
	total := 0
	for _, value := range slice {
		total += value
	}
	return total
}

func stringToSlice(id string, reverse bool) ([]int, error) {
	var slice []int
	for _, char := range id {
		val, err := strconv.Atoi(string(char))
		if err != nil {
			return nil, err
		}
		slice = append(slice, val)
	}
	if reverse {
		slices.Reverse(slice)
	}
	return slice, nil
}

func Valid(id string) bool {
	id = strings.ReplaceAll(id, " ", "")
	if !isValidLength(id) {
		return false
	}

	creditCard, err := stringToSlice(id, true)
	if err != nil {
		return false
	}
	for i, value := range creditCard {
		if i%2 != 0 {
			num := value * 2
			if num > 9 {
				num = num - 9
			}
			creditCard[i] = num
		}
	}
	total := sumSlice(creditCard)
	if total%10 == 0 {
		return true
	}
	return false
}
