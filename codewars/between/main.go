package main

import "fmt"

func Between(a, b int) []int {
	if a == b {
		return []int{b}
	}
	return append([]int{a}, Between(a+1, b)...)
}

func main() {
	fmt.Println(Between(1, 4))
}
