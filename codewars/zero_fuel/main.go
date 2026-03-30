package main

import "fmt"

func ZeroFuel(distanceToPump int, mpg int, fuelLeft int) bool {
	return distanceToPump <= (mpg * fuelLeft)
}

func main() {
	fmt.Println(ZeroFuel(50, 25, 2))
	fmt.Println(ZeroFuel(70, 25, 1))
}
