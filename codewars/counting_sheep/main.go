package main

import "fmt"

func CountSheeps(numbers []bool) int {
	var counter int

	for _, sheep := range numbers {
		if sheep {
			counter++
		}
	}

	return counter
}

func main() {
	farm := []bool{true, true, true, false,
		true, true, true, true,
		true, false, true, false,
		true, false, false, true,
		true, true, true, true,
		false, false, true, true}
	
	fmt.Println(CountSheeps(farm))
}
