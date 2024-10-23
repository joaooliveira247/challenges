package series

func All(n int, s string) []string {
	var allSub []string

	for len(s) >= n {
		allSub = append(allSub, s[:n])
		s = s[1:]
	}
	return allSub
}

func UnsafeFirst(n int, s string) string {
	return s[:n]
}
