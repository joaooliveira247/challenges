package main

import "fmt"

func genPoints(level int, magicItemLevel int) []int {
	points := []int{}

	if magicItemLevel == 0 {
		return []int{0}
	}

	for i := 1; magicItemLevel*i < level; i++ {
		points = append(points, magicItemLevel*i)
	}

	return points
}

func merge(arrays ...[]int) []int {
	newArray := []int{}
	for _, array := range arrays {
		for _, val := range array {
			newArray = append(newArray, val)
		}
	}

	return newArray
}

func removeDuplicates(array []int) []int {
	counter := map[int]int{}

	for _, val := range array {
		counter[val] += 1
	}

	newArray := []int{}

	for key, _ := range counter {
		newArray = append(newArray, key)
	}

	return newArray

}

func SumMultiples(limit int, divisors ...int) int {

	var magicPoints [][]int

	for _, val := range divisors {
		magicPoints = append(magicPoints, genPoints(limit, val))
	}

	mergedPoints := merge(magicPoints...)

	mergedPoints = removeDuplicates(mergedPoints)

	points := 0

	for _, val := range mergedPoints {
		points += val
	}

	return points
}

func main() {
	result := SumMultiples(1, 0)
	fmt.Println(result)
	// result := genPoints(1, 0)
	// fmt.Println(result)
}
