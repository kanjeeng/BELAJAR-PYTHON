package main

import "fmt"

func main() {
	var menu, tagihan, rombongan, i, n int
	var sisa bool
	fmt.Scan(&rombongan)
	for i = 1; i <= rombongan; i++ {
		fmt.Scan(&menu, &n, &sisa)
		hitungTarif_1303223064(menu, sisa, n, &tagihan)
		fmt.Println(tagihan)
	}
}

func tarif__1303223064(menu int) int {
	if menu <= 3 {
		return 10000
	} else if menu > 3 && menu <= 50 {
		return 10000 + (menu-3)*2500
	} else {
		return 100000
	}
}

func hitungTarif_1303223064(menu int, bersisa bool, n int, total *int) {
	if bersisa {
		*total = n * tarif__1303223064(menu)
	} else {
		*total = tarif__1303223064(menu)
	}
}
