package main

import "fmt"

func MakeNegative(x int) int {
	if x < 0 {
		return x
	}
	return x * -1
}

func main() {
	fmt.Println(MakeNegative(1))
	fmt.Println(MakeNegative(10))
	fmt.Println(MakeNegative(-5))
}
