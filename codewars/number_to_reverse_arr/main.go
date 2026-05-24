package main

import "fmt"

func Digitize(n int) []int {
	if n < 10 {
		return []int{n}
	}

	return append([]int{n % 10}, Digitize(n / 10)...)
}

func main() {
	fmt.Println(Digitize(35232))
	fmt.Println(Digitize(0))
}