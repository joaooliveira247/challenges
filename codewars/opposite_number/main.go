package main

import "fmt"

func Opposite(value int) int {
	return value * -1
}

func main() {
	testValues := []int{
		1, 14, -34,
	}

	for _, testValue := range testValues {
		fmt.Printf("(%d) | Result: %d\n", testValue, Opposite(testValue))
	}
}
