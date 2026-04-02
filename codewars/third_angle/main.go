package main

import "fmt"

func OtherAngle(a, b int) int {
	return 180 - (a + b)
}

func main() {
	fmt.Println(OtherAngle(30, 60))
	fmt.Println(OtherAngle(10, 20))
}
