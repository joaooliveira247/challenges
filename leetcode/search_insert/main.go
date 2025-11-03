package main

import "fmt"

func searchInsert(nums []int, target int) int {
	for idx, value := range nums {
		if value == target {
			return idx
		}

		if value > target {
			return idx
		}
	}
	return len(nums)
}

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 2))
}
