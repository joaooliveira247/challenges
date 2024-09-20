package diffsquares

import "math"

func SquareOfSum(n int) int {
	sumNaturals := 0
	for i := 1; i < n+1; i++ {
		sumNaturals += i
	}
	return int(math.Pow(float64(sumNaturals), 2))
}

func SumOfSquares(n int) int {
	sumNaturals := 0
	for i := 1; i < n+1; i++ {
		sumNaturals += int(math.Pow(float64(i), 2))
	}
	return sumNaturals
}

func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
