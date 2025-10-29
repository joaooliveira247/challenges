package main

import "fmt"

func removeElement(nums []int, val int) int {
	freeIndex := 0
	k := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[freeIndex] = nums[i]
			freeIndex++
			k++
		}
	}
	return k
}

func main() {
	arr := []int{3, 2, 2, 3}
	fmt.Println(removeElement(arr, 3), arr)
}
