package prime

func Factors(n int64) []int64 {
	var factors []int64
	i := int64(2)
	for n > 1 {
		if n%i == 0 {
			n = n / i
			factors = append(factors, i)
		} else {
			i++
		}
	}
	return factors
}
