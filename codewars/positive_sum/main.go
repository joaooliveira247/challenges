package main

import "fmt"

func PositiveSum(numbers []int) int {
	var sum int

	for _, val := range numbers {
		if val > 0 {
			sum += val
		}
	}

	return sum
}

func main() {
	fmt.Println(PositiveSum([]int{1, -4, 7, 12}))
}
