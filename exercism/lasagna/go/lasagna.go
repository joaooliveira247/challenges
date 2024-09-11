package lasagna

// TODO: define the 'OvenTime' constant
const (
	OvenTime             = 40
	LayerPreparationTime = 2
)

// RemainingOvenTime returns the remaining minutes based on the `actual`
// minutes already in the oven.
func RemainingOvenTime(actualMinutesInOven int) int {
	return OvenTime - actualMinutesInOven
}

// PreparationTime calculates the time needed to prepare the lasagna based on
// the amount of layers.
func PreparationTime(numberOfLayers int) int {
	return LayerPreparationTime * numberOfLayers
}

// ElapsedTime calculates the time elapsed cooking the lasagna. This time
// includes the preparation time and the time the lasagna is baking in the oven.
func ElapsedTime(numberOfLayers, actualMinutesInOven int) int {
	return actualMinutesInOven + (numberOfLayers * LayerPreparationTime)
}
