package main

import "fmt"

func FindMultiples(integer, limit int) []int {
	var result []int
	// (2, 6) -> [2, 4, 6]
	// (2, 5) -> [2, 4]
	for i := 1; i <= (limit / integer); i++ {
		result = append(result, integer * i)
	}
	return result
}

func main() {
	fmt.Println(FindMultiples(2,6))
	fmt.Println(FindMultiples(2,5))
	fmt.Println(FindMultiples(5,25))
	fmt.Println(FindMultiples(1,2))
}
