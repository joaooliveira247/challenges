package strain

// Implement the "Keep" and "Discard" function in this file.

// You will need typed parameters (aka "Generics") to solve this exercise.
// They are not part of the Exercism syllabus yet but you can learn about
// them here: https://go.dev/tour/generics/1
func Keep[T any](collection []T, predicade func(T) bool) []T {
	newCollection := []T{}
	for _, value := range collection {
		if predicade(value) {
			newCollection = append(newCollection, value)
		}
	}
	return newCollection
}

func Discard[T any](collection []T, predicade func(T) bool) []T {
	newCollection := []T{}
	for _, value := range collection {
		if !predicade(value) {
			newCollection = append(newCollection, value)
		}
	}
	return newCollection
}
