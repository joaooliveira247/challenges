package main

import "fmt"

func ReverseSeq(n int) []int {
	if n == 1 {
		return []int{1}
	}

	return append([]int{n}, ReverseSeq(n-1)...)
}

func main() {
	fmt.Println(ReverseSeq(5))
}
