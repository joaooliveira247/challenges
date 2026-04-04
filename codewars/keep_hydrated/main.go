package main

import (
	"fmt"
)

func Litres(time float64) int {
	return int(time * 0.5)
}

func main() {
	fmt.Println(Litres(3))
	fmt.Println(Litres(6.7))
	fmt.Println(Litres(11.8))
}
