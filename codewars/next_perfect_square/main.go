package main

import (
	"fmt"
	"math"
)

func FindNextSquare(sq int64) int64 {
	if root := math.Sqrt(float64(sq)); math.Mod(root, 1) == 0 {
		next := int64(root + 1)
		return next * next
	}
	return -1
}

func main() {
	fmt.Println(FindNextSquare(121))
	fmt.Println(FindNextSquare(625))
	fmt.Println(FindNextSquare(114))
}
