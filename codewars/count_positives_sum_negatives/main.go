package main

import "fmt"

func CountPositivesSumNegatives(numbers []int) []int {
	var res []int
	var countPositives int
	var sumNegatives int

	for _, num := range numbers {
		if num > 0 {
			countPositives++
			continue
		}
		sumNegatives += num
	}

	res = append(res, countPositives, sumNegatives)

	return res // your code here
}

func main() {
	fmt.Println(CountPositivesSumNegatives([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15}))
}
