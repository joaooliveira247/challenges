package main

import "fmt"

func Invert(arr []int) []int {
	if len(arr) < 1 {
		return []int{}
	}
	return append([]int{arr[0] * -1}, Invert(arr[1:])...)
}

func main() {
	fmt.Println(Invert([]int{1, 2, 3, 4, 5}))
	fmt.Println(Invert([]int{1, -2, 3, -4, 5}))
	fmt.Println(Invert([]int{}))
}
