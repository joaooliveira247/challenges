package main

import "fmt"

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func Strong(n int) string {
	num := n
	var total int

	for num > 0 {
		total += factorial(num % 10)
		num = num / 10
	}

	if total == n {
		return "STRONG!!!!"
	}
	return "Not Strong !!"
}

func main() {
	fmt.Println(Strong(123))
	fmt.Println(Strong(1))
	fmt.Println(Strong(145))
}
