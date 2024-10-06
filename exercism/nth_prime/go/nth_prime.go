package prime

import (
	"errors"
	"math"
)

func isPrime(n int) bool {
	for i := 2; i < int(math.Pow(float64(n), 0.5))+1; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// Nth returns the nth prime number. An error must be returned if the nth prime number can't be calculated ('n' is equal or less than zero)
func Nth(n int) (int, error) {
	if n < 1 {
		return 0, errors.New("value is lower than 1")
	}
	num := 2
	count := 0

	for {
		if isPrime(num) {
			count++
			if count == n {
				return num, nil
			}
		}
		num++
	}
}
