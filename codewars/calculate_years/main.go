package main

import "fmt"

func CalculateYears(years int) (result [3]int) {
	for i := 0; i < years; i++ {
		switch i {
		case 0:
			result[1] += 15
			result[2] += 15
		case 1:
			result[1] += 9
			result[2] += 9
		default:
			result[1] += 4
			result[2] += 5
		}
	}

	result[0] += years

	return result
}

func main() {
	fmt.Println(CalculateYears(1))
	fmt.Println(CalculateYears(2))
	fmt.Println(CalculateYears(10))
}
