package etl

import "strings"

func Transform(in map[int][]string) map[string]int {
	newMap := map[string]int{}
	for point, slice := range in {
		for _, letter := range slice {
			newMap[strings.ToLower(letter)] = point
		}
	}
	return newMap
}
