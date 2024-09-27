package grains

import (
	"errors"
	"math"
)

func Square(number int) (uint64, error) {
	if number < 1 || number > 64 {
		return 0, errors.New("out of range")
	}
	return uint64(math.Pow(2, float64(number-1))), nil
}

func Total() uint64 {
	boardtotal := 0
	for i := 1; i <= 64; i++ {
		val, _ := Square(i)
		boardtotal += int(val)
	}
	return uint64(boardtotal)
}
