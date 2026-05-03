package main

import "fmt"

func hammingWeight(n int) (counter int) {
	bitNum := fmt.Sprintf("%b", n)

	for _, b := range bitNum {
		if b == '1' {
			counter++
		}
	}

	return counter
}

func main() {
	fmt.Println(hammingWeight(11))
	fmt.Println(hammingWeight(2147483645))
}
