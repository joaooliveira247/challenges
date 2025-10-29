package main

import (
	"fmt"
	"strconv"
)

func smallestNumber(n int) int {
	binaryString := strconv.FormatInt(int64(n), 2)

	var newBinary string

	for i := 0; i < len(binaryString); i++ {
		newBinary += "1"
	}

	num, _ := strconv.ParseInt(newBinary, 2, 64)

	return int(num)
}

func main() {
	fmt.Println(smallestNumber(5))
}
