package raindrops

import (
	"fmt"
	"strings"
)

func Convert(number int) string {
	values := map[int]string{
		3: "Pling", 5: "Plang", 7: "Plong",
	}
	var result []string

	for key, value := range values {
		if number%key == 0 {
			result = append(result, value)
		}
	}
	if len(result) == 0 {
		return fmt.Sprintf("%d", number)
	}
	return strings.Join(result, "")
}
