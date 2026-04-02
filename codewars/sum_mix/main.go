package main

import (
	"fmt"
	"strconv"
)

func SumMix(arr []any) (total int) {
	for _, value := range arr {
		switch v := value.(type) {
		case int:
			total += v
			continue
		case string:
			num, _ := strconv.Atoi(v)
			total += num
			continue
		}
	}
	return total
}

func main() {
	fmt.Println(SumMix([]any{9, 3, "7", "3"}))
}
