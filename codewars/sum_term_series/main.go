package main

import "fmt"

func seriesSumFloat(n int) float64 {
	if n == 0 {
		return 0
	}
	return 1.0/((3.0*float64(n))-2.0) + seriesSumFloat(n-1)
}

func SeriesSum(n int) string {
	// your code here
	return fmt.Sprintf("%.2f", seriesSumFloat(n))
}

func main() {
	fmt.Println(SeriesSum(1))
	fmt.Println(SeriesSum(2))
	fmt.Println(SeriesSum(4))
}
