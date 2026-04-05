package main

import "fmt"

func Digits(n uint64) (counter int) {
	if n == 0 {
		return 1
	}
	for n > 0 {
		counter++
		n = n / 10
	}
	return counter
}

func main() {
	fmt.Println(Digits(66))
	fmt.Println(Digits(7))
	fmt.Println(Digits(0))
	fmt.Println(Digits(123456))
}
