package main

import "fmt"

func combat(health, damage float64) float64 {
	if result := health - damage; result > 0 {
		return result
	}
	return 0
}

func main() {
	fmt.Println(combat(100.0, 50.0))
	fmt.Println(combat(1.0, 100))
}
