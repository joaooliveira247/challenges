package main

import "fmt"

func GetSum(a, b int) int {
	var sum int
	var initialValue int
	var endValue int

	if a < b {
		initialValue = a
		endValue = b
	} else {
		initialValue = b
		endValue = a
	}

	for i := initialValue; i <= endValue; i++ {
		sum += i
	}

	return sum
}

func main() {
	fmt.Println(GetSum(1, 0))
	fmt.Println(GetSum(1, 2))
	fmt.Println(GetSum(0, 1))
	fmt.Println(GetSum(-1, 2))
}
