package main

import "fmt"

func CheckForFactor(base, factor int) bool {
	return base%factor == 0
}

func main() {
	fmt.Println(CheckForFactor(10, 2))
	fmt.Println(CheckForFactor(24617, 3))
}
