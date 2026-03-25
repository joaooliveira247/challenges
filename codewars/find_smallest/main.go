package main

import "fmt"

func SmallestIntegerFinder(numbers []int) int {

	if len(numbers) < 2 {
		return numbers[0]
	}

	if numbers[0] < numbers[1] {
		return SmallestIntegerFinder(append(numbers[2:], numbers[0]))
	}
	return SmallestIntegerFinder(numbers[1:])

}

func main() {
	fmt.Println(SmallestIntegerFinder([]int{34, -345, -1, 100}))
}
