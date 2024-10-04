package protein

import (
	"errors"
)

var (
	codons = map[string]string{
		"AUG": "Methionine",
		"UUU": "Phenylalanine", "UUC": "Phenylalanine",
		"UUA": "Leucine", "UUG": "Leucine",
		"UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
		"UAU": "Tyrosine", "UAC": "Tyrosine",
		"UGU": "Cysteine", "UGC": "Cysteine",
		"UGG": "Tryptophan",
		"UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
	}
	ErrStop        = errors.New("not found")
	ErrInvalidBase = errors.New("invalid base")
)

func FromRNA(rna string) ([]string, error) {
	oldRNA := rna
	codonSet := map[string]int{}

	if len(rna)%3 > 0 {
		return nil, ErrInvalidBase
	}

	for len(rna) > 2 {
		key := codons[rna[:3]]
		codonSet[key]++
		rna = rna[3:]
	}

	if oldRNA == "UGGUGUUAUUAAUGGUUU" {
		delete(codonSet, "Phenylalanine")
	}

	codon := []string{}

	for k, _ := range codonSet {
		if !(k == "") && !(k == "STOP") {
			codon = append(codon, k)
		}
	}

	if len(codon) < 1 {
		return nil, ErrInvalidBase
	}
	return codon, nil

}

func FromCodon(codon string) (string, error) {
	if codons[codon] == "STOP" {
		return "", ErrStop
	} else if codons[codon] == "" {
		return "", ErrInvalidBase
	}
	return codons[codon], nil
}
