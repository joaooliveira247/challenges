package main

import "fmt"

func Derive(coeficient, expoent int) string {
	return fmt.Sprintf("%dx^%d", coeficient*expoent, expoent-1)
}

func main() {
	fmt.Println(Derive(7, 8))
	fmt.Println(Derive(5, 9))
}
