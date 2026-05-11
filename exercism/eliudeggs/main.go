package main

import "fmt"

func EggCount(displayValue int) (count int) {
	for _, char := range fmt.Sprintf("%b", displayValue) {
		if char == '1' {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(EggCount(89))
	fmt.Println(EggCount(8))
}
