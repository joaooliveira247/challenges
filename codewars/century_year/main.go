package main

import "fmt"

func century(year int) int {
	// Finish this :)
	if year%100 >= 1 {
		return (year / 100) + 1
	} else {
		return year / 100
	}
}

func main() {

	years := []int{1705, 1900, 1601, 2000, 2742}

	for _, year := range years {
		fmt.Println(century(year))
	}
}
