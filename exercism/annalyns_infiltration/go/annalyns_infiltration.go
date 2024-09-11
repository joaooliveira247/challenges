package annalyn

// CanFastAttack can be executed only when the knight is sleeping.
func CanFastAttack(knightIsAwake bool) bool {
	return !knightIsAwake
}

// CanSpy can be executed if at least one of the characters is awake.
func CanSpy(knightIsAwake, archerIsAwake, prisonerIsAwake bool) bool {
	group := [3]bool{knightIsAwake, archerIsAwake, prisonerIsAwake}

	for _, status := range group {
		if status != false {
			return true
		}
	}
	return false
}

// CanSignalPrisoner can be executed if the prisoner is awake and the
// archer is sleeping.
func CanSignalPrisoner(archerIsAwake, prisonerIsAwake bool) bool {
	if !archerIsAwake && prisonerIsAwake {
		return true
	}
	return false
}

// CanFreePrisoner can be executed if the prisoner is awake and the other 2
// characters are asleep
// or if Annalyn's pet dog is with her and the archer is sleeping.
func CanFreePrisoner(
	knightIsAwake, archerIsAwake, prisonerIsAwake, petDogIsPresent bool,
) bool {
	if prisonerIsAwake && !knightIsAwake && !archerIsAwake {
		return true
	} else if petDogIsPresent && !archerIsAwake {
		return true
	} else {
		return false
	}
}
