package phonenumber

import (
	"errors"
	"fmt"
	"strings"
	"unicode"
)

func extractNumbers(s string) (string, error) {
	var number strings.Builder
	for _, char := range s {
		if unicode.IsNumber(char) {
			number.WriteRune(char)
		}
	}

	if length := len(number.String()); length > 11 || length < 10 {
		return "", errors.New("invalid phone number")
	}
	return number.String(), nil
}

// use regex
func Number(phoneNumber string) (string, error) {
	number, err := extractNumbers(phoneNumber)

	if err != nil {
		return "", err
	}

	_, err = AreaCode(phoneNumber)

	if err != nil {
		return "", err
	}

	if len(number) == 11 {
		return number[1:], nil
	}

	return number, nil
}

func AreaCode(phoneNumber string) (string, error) {
	//verify area code first, and call in number to check it
	numbers, err := extractNumbers(phoneNumber)

	if err != nil {
		return "", errors.New("invalid phone number")
	}

	var codeArea string

	if len(numbers) == 11 {
		if numbers[0] != '1' || numbers[1] < 50 || numbers[4] < 50 {
			return "", errors.New("invalid phone number")
		}
		codeArea = numbers[1:4]
	} else {
		if numbers[0] < 50 || numbers[3] < 50 {
			return "", errors.New("invalid phone number")
		}
		codeArea = numbers[:3]
	}

	return codeArea, nil
}

func Format(phoneNumber string) (string, error) {
	numbers, err := extractNumbers(phoneNumber)

	if err != nil {
		return "", errors.New("invlaid phone number")
	}

	codeArea, err := AreaCode(phoneNumber)

	if err != nil {
		return "", errors.New("invlaid phone number")
	}

	if len(numbers) == 11 {
		return fmt.Sprintf("+1 (%s) %s-%s", codeArea, numbers[4:7], numbers[7:]), nil
	}
	return fmt.Sprintf("(%s) %s-%s", codeArea, numbers[2:5], numbers[6:]), nil
}
