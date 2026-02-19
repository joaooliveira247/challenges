package main

import "fmt"

func mySqrt(x int) int {

	if x <= 1 {
		return x
	}

	left := 0

	right := x

	for left <= right {
		mid := (left + right) / 2

		if (mid * mid) == x {
			return mid
		} else if mid == left {
			return mid
		}

		if (mid * mid) > x {
			right = mid
		} else {
			left = mid
		}

	}

	return 0
}

func main() {
	fmt.Println(mySqrt(12))
}
