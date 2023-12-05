package main

import "fmt"

func main() {
	var num, num1, num2 int
	fmt.Scanln(&num)
	split_1303223064(num, &num1, &num2)
	fmt.Println(num1, num2)
	fmt.Println(num1 + num2)
}
func len_1303223064(num int) int {
	var total int = 0

	for num > 0 {
		total++
		num /= 10
	}
	return total
}
func pangkat_1303223064(n int) int {
	var total int = 1
	for n > 0 {
		total *= 10
		n--
	}
	return total
}
func split_1303223064(num int, num1, num2 *int) {
	var mid int = len_1303223064(num) / 2
	*num1 = num / pangkat_1303223064(mid)
	*num2 = num % pangkat_1303223064(mid)
}
