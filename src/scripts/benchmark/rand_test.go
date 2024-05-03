package benchmark_test

import (
	"benchmark"
	"fmt"
	"os"
	"testing"
)

func BenchmarkMathRand(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		benchmark.MathRand()
	}
}

func BenchmarkCryptoRand(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		benchmark.CryptoRand()
	}
}

func BenchmarkLCG(b *testing.B) {
	lcg := benchmark.NewLCG(1, 75, 74, 1<<16+1)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		lcg.Gen()
	}
}

func BenchmarkMSM(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		benchmark.MSM()
	}
}

func BenchmarkMercenneTwister(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		benchmark.MercenneTwister()
	}
}

func TestLCGFuzz(t *testing.T) {
	lcg := benchmark.NewLCG(1, 75, 74, 1<<16+1)

	t.Run("2^16", func(t *testing.T) {
		file, err := os.OpenFile("../../data/zx/lcg_2_16.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 16
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^4", func(t *testing.T) {
		file, err := os.OpenFile("../../data/zx/lcg_2_4.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 4
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^8", func(t *testing.T) {
		file, err := os.OpenFile("../../data/zx/lcg_2_8.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 8
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^12", func(t *testing.T) {
		file, err := os.OpenFile("../../data/zx/lcg_2_12.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 12
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})
}

func TestLCGFuzz2(t *testing.T) {
	lcg := benchmark.NewLCG(1, 101, 49, 20040213)

	t.Run("2^16", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand/lcg_2_16.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 16
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^4", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand/lcg_2_4.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 4
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^8", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand/lcg_2_8.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 8
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^12", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand/lcg_2_12.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 12
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})
}

func TestLCGFuzz3(t *testing.T) {
	lcg := benchmark.NewLCG(1, 1000, 2103, 20040213)

	t.Run("2^16", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand2/lcg_2_16.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 16
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^4", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand2/lcg_2_4.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 4
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^8", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand2/lcg_2_8.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 8
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})

	t.Run("2^12", func(t *testing.T) {
		file, err := os.OpenFile("../../data/rand2/lcg_2_12.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			t.Fatal(err)
		}
		defer file.Close()

		n := 1 << 12
		for i := 0; i < n; i++ {
			val := lcg.Gen()
			file.WriteString(fmt.Sprint(val, "\n"))
		}
	})
}
