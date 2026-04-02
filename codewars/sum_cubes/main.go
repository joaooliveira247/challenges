package main

import "fmt"

func powCube(n int) int {
	return n * n * n
}

func SumCubes(n int) (total int) {
	if n == 1 {
		return 1
	}
	return powCube(n) + SumCubes(n-1)
}

func main() {
	fmt.Println(SumCubes(2))
	fmt.Println(SumCubes(3))
}
