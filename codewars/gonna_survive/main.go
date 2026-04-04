package main

import "fmt"

func Hero(bullets, dragons int) bool {
	return bullets >= dragons*2
}

func main() {
	fmt.Println(Hero(10, 5))
	fmt.Println(Hero(7, 4))
}
