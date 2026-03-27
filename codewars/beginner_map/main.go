package main

import "fmt"

func Maps(x []int) []int {
	if len(x) == 1 {
		return []int{2 * x[0]}
	}
	return append([]int{x[0] * 2}, Maps(x[1:])...)
}

func main() {
	fmt.Println(Maps([]int{1, 2, 3}))
}
