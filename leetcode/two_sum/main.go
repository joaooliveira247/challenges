package main

import "fmt"

func twoSum(nums []int, target int) []int {
	for idx, _ := range nums[:len(nums)-1] {
		for interIdx, value := range nums[idx+1:] {
			if nums[idx]+value == target {
				return []int{idx, interIdx + (idx + 1)}
			}
		}
	}
	return nil
}

func main() {
	// first create function that verify one target in array
	// after separa it in two functions

	arr := []int{2, 7, 11, 15}
	target := 9

	fmt.Println(twoSum(arr, target))

}
