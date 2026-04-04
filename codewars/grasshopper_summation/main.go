package main

import "fmt"

func Summation(n int) int {
	if n == 0 {
		return 0
	}
	return n + Summation(n-1)
}

func main() {
	fmt.Println(Summation(2))
	fmt.Println(Summation(8))
}
