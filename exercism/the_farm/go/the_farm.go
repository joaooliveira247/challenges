package thefarm

import "fmt"

type MyCustomError struct {
	msg string
}

type InvalidCowsError struct {
	cows int
	msg  string
}

func (myError *MyCustomError) Error() string {
	return myError.msg
}

func (myError *InvalidCowsError) Error() string {
	return fmt.Sprintf("%d cows are invalid: %s", myError.cows, myError.msg)
}

// TODO: define the 'DivideFood' function
func DivideFood(fc FodderCalculator, cows int) (float64, error) {
	amount, err := fc.FodderAmount(cows)
	if err != nil {
		return 0, err
	}

	ff, err := fc.FatteningFactor()
	if err != nil {
		return 0, err
	}

	return (amount * ff) / float64(cows), nil
}

// TODO: define the 'ValidateInputAndDivideFood' function
func ValidateInputAndDivideFood(
	fc FodderCalculator,
	cows int,
) (float64, error) {
	if cows <= 0 {
		return 0, &MyCustomError{"invalid number of cows"}
	}
	divide, err := DivideFood(fc, cows)
	if err != nil {
		return 0, err
	}
	return divide, nil

}

// TODO: define the 'ValidateNumberOfCows' function
func ValidateNumberOfCows(cows int) error {
	if cows < 0 {
		return &InvalidCowsError{cows: cows, msg: "there are no negative cows"}
	} else if cows == 0 {
		return &InvalidCowsError{cows: cows, msg: "no cows don't need food"}
	} else {
		return nil
	}
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
