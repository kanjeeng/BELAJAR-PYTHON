package main

import "fmt"

func main() {
	var jam, menit int
	var member bool
	var total float64
	fmt.Scan(&jam, &menit, &member)
	hitungSewa__1303223064(jam, menit, member, &total)

	fmt.Println(total)
}

func durasi_1303223064(jam, menit int) int {
	if jam == 0 && menit != 0 {
		return 1
	} else if menit >= 10 {
		return jam + 1
	}
	return jam
}

func potongan_1303223064(durasi, tarif int) float64 {
	if durasi > 3 {
		return float64(durasi*tarif) * 0.1
	}
	return 0
}

func tarif__1303223064(member bool) int {
	if member {
		return 3500
	}
	return 5000
}
func hitungSewa__1303223064(jam, menit int, member bool, biaya *float64) {
	var durasi int = durasi_1303223064(jam, menit)
	var tarif int = tarif__1303223064(member)
	var diskon float64 = potongan_1303223064(durasi, tarif)
	*biaya = float64(durasi*tarif) - diskon
}
