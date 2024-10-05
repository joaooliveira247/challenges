package lsproduct

import (
	"errors"
	"strconv"
)

func LargestSeriesProduct(digits string, span int) (int64, error) {
	if len(digits) < span || span < 0 {
		return 0, errors.New(
			"span must be smaller than string length or span negative",
		)
	}

	series := []string{}

	for len(digits) >= span {
		series = append(series, digits[:span])
		digits = digits[1:]
	}

	var largest int

	for _, serie := range series {
		total := 1
		for _, num := range serie {
			numConv, err := strconv.Atoi(string(num))
			if err != nil {
				return 0, err
			}
			total *= numConv
		}
		if total > largest {
			largest = total
		}
	}
	return int64(largest), nil

}
