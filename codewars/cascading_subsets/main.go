package main

import "fmt"

func EachCons(arr []int, n int) [][]int {
	if len(arr) < n {
		return [][]int{}
	}
	// [1, 2, 3, 4], 3 -> [[1, 2, 3], [2, 3, 4]]
	if len(arr) == n {
		return [][]int{arr}
	}
	return append([][]int{arr[:n]}, EachCons(arr[1:], n)...)
}

func main() {
	fmt.Println(EachCons([]int{1, 2, 3, 4}, 3))
	fmt.Println(EachCons([]int{1, 2, 3, 4}, 2))
}
