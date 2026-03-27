package main

import (
	"fmt"
)

func Pow(n int) uint64 {
	total := 2
	for i := 1; i < n; i++ {
		total *= 2
	}
	return uint64(total)
}

func PowersOfTwo(n int) []uint64 {
	if n == 0 {
		return []uint64{1}
	}
	return append(PowersOfTwo(n-1), Pow(n))
}

func main() {
	fmt.Println(PowersOfTwo(4))
}
