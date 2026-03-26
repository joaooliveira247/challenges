package main

import (
	"fmt"
	"strings"
)

func countSheep(num int) string {
	var text strings.Builder

	for idx := 1; idx <= num; idx++ {
		text.WriteString(fmt.Sprintf("%d sheep...", idx))
	}

	return text.String()

}

func main() {
	fmt.Println(countSheep(3))
}
