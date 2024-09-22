package strand

func ToRNA(dna string) string {
	newDNA := []rune(dna)
	toReplace := map[rune]rune{
		'G': 'C',
		'C': 'G',
		'T': 'A',
		'A': 'U',
	}

	for i, value := range dna {
		newDNA[i] = toReplace[value]
	}
	return string(newDNA)
}
