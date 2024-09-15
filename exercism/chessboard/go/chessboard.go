package chessboard

// Declare a type named File which stores if a square is occupied by a piece - this will be a slice of bools
type File []bool

// Declare a type named Chessboard which contains a map of eight Files, accessed with keys from "A" to "H"
type Chessboard map[string]File

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) int {
	counter := 0
	for _, value := range cb[file] {
		if value {
			counter++
		}
	}
	return counter
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) int {
	counter := 0
	if rank < 1 || rank > 8 {
		return counter
	}

	for _, file := range cb {
		if file[rank-1] {
			counter++
		}
	}
	return counter
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
	counter := 0

	for _, file := range cb {
		counter += len(file)
	}
	return counter
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {
	counter := 0
	for _, file := range cb {
		for _, square := range file {
			if square {
				counter++
			}
		}
	}
	return counter
}
