package main

import (
	"fmt"
	"math/big"
)

func addBinary(a string, b string) string {

	aBig := new(big.Int)
	bBig := new(big.Int)

	aBig.SetString(a, 2)
	bBig.SetString(b, 2)

	sum := new(big.Int).Add(aBig, bBig)

	return sum.Text(2)
}

func main() {
	a := "11"
	b := "1"

	fmt.Println(addBinary(a, b))
}
