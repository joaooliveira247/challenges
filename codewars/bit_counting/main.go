package main

import "fmt"

func CountBits(n uint) int {
	mapValue := map[string]int{}
	for _, value := range fmt.Sprintf("%b", n) {
		mapValue[string(value)]++
	}

	return mapValue["1"]
}

func main() {
	fmt.Println(CountBits(1234))
}
