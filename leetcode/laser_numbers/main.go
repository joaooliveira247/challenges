package main

import "fmt"

func countNumberOfDevices(layer string) int {
	var counter int
	for _, char := range layer {
		if char == 49 {
			counter++
		}
	}
	return counter
}

func numberOfBeams(bank []string) int {
	var counter int
	currentLayer := countNumberOfDevices(bank[0])

	for _, devices := range bank[1:] {
		counter += currentLayer * countNumberOfDevices(devices)
		if numDevices := countNumberOfDevices(devices); numDevices > 0 {
			currentLayer = numDevices
		}
	}
	return counter
}

func main() {
	bank := []string{"011001", "000000", "010100", "001000"}
	fmt.Println(numberOfBeams(bank))
}
