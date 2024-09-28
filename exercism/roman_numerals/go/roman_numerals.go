package romannumerals

import (
	"errors"
	"strings"
)

func evalUnits(num int) string {
	// I(1), II(2), III(3), IV(4), V(5), VI(6), VII(7), VIII(8), IX(9)
	eval := map[int]string{
		1: "I",
		4: "IV",
		5: "V",
		9: "IX",
	}
	if num < 4 {
		return strings.Repeat(eval[1], num)
	} else if num == 4 || num == 9 {
		return eval[num]
	} else {
		return eval[5] + strings.Repeat(eval[1], num%5)
	}
}

func evalTens(num int) string {
	eval := map[int]string{
		10: "X",
		40: "XL",
		50: "L",
		90: "XC",
	}
	val := num / 10
	if val < 4 {
		return strings.Repeat(eval[10], val)
	} else if val == 4 || val == 9 {
		return eval[val*10]
	} else {
		return eval[50] + strings.Repeat(eval[10], val%5)
	}
}

func evalHundreds(num int) string {
	eval := map[int]string{
		100: "C",
		400: "CD",
		500: "D",
		900: "CM",
	}
	val := num / 100
	if val < 4 {
		return strings.Repeat(eval[100], val)
	} else if val == 4 || val == 9 {
		return eval[val*100]
	} else {
		return eval[500] + strings.Repeat(eval[100], val%5)
	}
}

func evalThousands(num int) string {
	return strings.Repeat("M", num/1000)
}

func ToRomanNumeral(input int) (string, error) {
	if input < 1 || input >= 4000 {
		return "", errors.New("out of range")
	}
	return evalThousands(
		input,
	) + evalHundreds(
		input%1000,
	) + evalTens(
		input%100,
	) + evalUnits(
		input%10,
	), nil
}
