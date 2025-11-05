package main

import (
	"fmt"
	"math/big"
	"strconv"
)

func plusOne(digits []int) []int {
	var numString string

	for _, value := range digits {
		numString += fmt.Sprintf("%d", value)
	}

	numBig := new(big.Int)
	numBig.SetString(numString, 10)
	numBig.Add(numBig, big.NewInt(1))

	var newArr []int

	for _, value := range numBig.String() {
		valueInt, _ := strconv.Atoi(string(value))
		newArr = append(newArr, valueInt)
	}

	return newArr
}

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))
	fmt.Println(plusOne([]int{9, 9}))
	fmt.Println(plusOne([]int{9}))
}
