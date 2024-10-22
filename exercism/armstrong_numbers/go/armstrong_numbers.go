package armstrong

import (
	"math"
	"strconv"
)

func IsNumber(n int) bool {
	decimals := strconv.Itoa(n)
	
	total := 0
	for _, decimal := range decimals {
		num, _ := strconv.Atoi(string(decimal))
		total += int(math.Pow(float64(num), float64(len(decimals)))) 
	}
	
	if total == n {
		return true
	}
	return false
}
