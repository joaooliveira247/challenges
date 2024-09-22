	package dna

	import "errors"

	func contains[T comparable](value T, slice []T) bool {
		for _, sliceValue := range slice {
			if sliceValue == value {
				return true
			}
		}
		return false
	}

	// Histogram is a mapping from nucleotide to its count in given DNA.
	// Choose a suitable data type.
	type Histogram map[rune]int

	// DNA is a list of nucleotides. Choose a suitable data type.
	type DNA string

	// Counts generates a histogram of valid nucleotides in the given DNA.
	// Returns an error if d contains an invalid nucleotide.
	// /
	// Counts is a method on the DNA type. A method is a function with a special receiver argument.
	// The receiver appears in its own argument list between the func keyword and the method name.
	// Here, the Counts method has a receiver of type DNA named d.
	func (d DNA) Counts() (Histogram, error) {
		var h Histogram = Histogram{'A': 0, 'C': 0, 'G': 0, 'T': 0}

		for _, char := range d {
			if letter := string(char); contains(
				letter,
				[]string{"A", "C", "G", "T"},
			) {
				h[char]++
			} else {
				return Histogram{'A': 0, 'C': 0, 'G': 0, 'T': 0}, errors.New("invalid nucleotide")
			}
		}

		return h, nil
	}
