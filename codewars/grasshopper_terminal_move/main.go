package main

import "fmt"

func Move(position int, roll int) int {
	return position + (2 * roll)
}

func main() {
	fmt.Println(Move(3, 6))
	fmt.Println(Move(0, 4))
}
