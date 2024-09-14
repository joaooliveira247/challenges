package lasagna

const (
	DefaultLayerPreparationTime = 2
	DefaultNoodleQuantity       = 50
	DefaultSauceQuantity        = 0.2
)

// Calcule Lasagna preparation time given layers ingredients and time per layer,
// default value for timePerLayer param is 2
func PreparationTime(layers []string, timePerLayer int) int {
	if timePerLayer > 0 {
		return len(layers) * timePerLayer
	}
	return len(layers) * DefaultLayerPreparationTime
}

// TODO: define the 'Quantities()' function
// Calcule quatities of noodles and sauce to prepare your meal.
func Quantities(layers []string) (int, float64) {
	quantity := make(map[string]int)
	for _, ingredient := range layers {
		quantity[ingredient] += 1
	}
	return DefaultNoodleQuantity * quantity["noodles"], DefaultSauceQuantity * float64(
		quantity["sauce"],
	)
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendList []string, myList []string) {
	myList[len(myList)-1] = friendList[len(friendList)-1]
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, portions int) []float64 {
	var newQuantities []float64
	for _, value := range quantities {
		newQuantities = append(newQuantities, value*(float64(portions)/2.0))
	}
	return newQuantities
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
