package main

import "fmt"

func MultiplicationTable(size int) [][]int {
	var iTable [][]int
	for i := 1; i <= size; i++ {
		var jTable []int
		for j := 1; j <= size; j++ {
			jTable = append(jTable, i*j)
		}
		iTable = append(iTable, jTable)
	}

	return iTable
}

func main() {
	fmt.Println(MultiplicationTable(1))
	fmt.Println(MultiplicationTable(3))
}
