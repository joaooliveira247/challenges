package sieve

import "math"

func isPrime(n int) bool {
	for i := 2; i < int(math.Pow(float64(n), 0.5))+1; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}


func Sieve(limit int) []int {
	var primes []int
	
	num := 2
	
	for num <= limit {
		if isPrime(num) {
			primes = append(primes, num)
		}
		num++
	}
	return primes
}
