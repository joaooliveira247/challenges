package main

import "fmt"

func Divisors(n int) (counter int) {
	for i := n; i > 0; i-- {
		if n%i == 0 {
			counter++
		}
	}
	return counter
}

func main() {
	fmt.Println(Divisors(4))
	fmt.Println(Divisors(5))
	fmt.Println(Divisors(12))
	fmt.Println(Divisors(30))
}
