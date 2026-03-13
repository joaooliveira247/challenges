package main

import "fmt"

func NbYear(p0 int, percent float64, aug int, p int) int {

	var years int

	for p0 < p {
		pGrowth := int(float64(p0) * (percent / 100))
		p0 = p0 + pGrowth + aug
		years++
	}

	return years
}

func main() {
	fmt.Println(NbYear(1500, 5, 100, 5000))
	fmt.Println(NbYear(1500000, 2.5, 10000, 2000000))
}
