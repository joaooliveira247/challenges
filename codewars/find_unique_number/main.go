package main

import "fmt"

func FindUniq(arr []float32) float32 {
	uniq := map[float32]int{}

	for _, v := range arr {
		uniq[v]++
	}

	for k, v := range uniq {
		if v == 1 {
			return k
		}
	}

	return -1
}

func main() {
	result := FindUniq([]float32{1, 1, 1, 1, 2, 1, 1})

	fmt.Println(result)
}
