package main

import "fmt"

func SimpleMultiplication(n int) int {
	if n%2 == 0 {
		return n * 8
	}

	return n * 9
}

func main() {
	fmt.Println(SimpleMultiplication(1))
	fmt.Println(SimpleMultiplication(3))
	fmt.Println(SimpleMultiplication(2))
	fmt.Println(SimpleMultiplication(22))
}
