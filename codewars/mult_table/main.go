package main

import (
	"fmt"
	"strings"
)

func MultiTable(number int) string {
	//good luck
	var table strings.Builder

	for i := 1; i <= 10; i++ {
		if i == 10 {
			fmt.Fprintf(&table, "%d * %d = %d", i, number, number*i)
			continue
		}
		fmt.Fprintf(&table, "%d * %d = %d\n", i, number, number*i)
	}

	return table.String()
}

func main() {
	fmt.Println(MultiTable(5))
}
