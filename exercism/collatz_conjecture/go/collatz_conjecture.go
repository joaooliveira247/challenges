package collatzconjecture

import "errors"

func CollatzConjecture(n int) (int, error) {
	if n <= 0 {
		return 0, errors.New("n cannot be lower or equal than 0")
	} else if n == 1 {
		return 0, nil
	}

	var counter int
	for n > 1 {
		counter++
		if n%2 == 0 {
			n = n / 2
		} else {
			n = (3 * n) + 1
		}
	}
	return counter, nil

}
