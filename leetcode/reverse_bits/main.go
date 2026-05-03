package main

import (
	"fmt"
	"strconv"
	"strings"
)

func reverseBits(n int) int {
	binaryStringNum := fmt.Sprintf("%032b", n)

	var reverseStringNum strings.Builder

	for i := len(binaryStringNum) - 1; i >= 0; i-- {
		reverseStringNum.WriteByte(binaryStringNum[i])
	}

	val, _ := strconv.ParseInt(reverseStringNum.String(), 2, 64)

	return int(val)
}

func main() {
	fmt.Println("43261596", reverseBits(43261596))
}
