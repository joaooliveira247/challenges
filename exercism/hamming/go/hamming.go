package hamming

import "errors"

func Distance(a, b string) (int, error) {
	if a == "" && b == "" {
		return 0, nil
	}
	if a == "" || b == "" {
		return 0, errors.New("strand cannot be empty")
	}
	if len(a) != len(b) || len(b) != len(a) {
		return 0, errors.New("strand with different sizes")
	}

	var counter int
	for i := range a {
		if a[i] != b[i] {
			counter++
		}
	}

	return counter, nil
}
