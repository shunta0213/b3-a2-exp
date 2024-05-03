package benchmark_test

import (
	"benchmark"
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
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		benchmark.LCG()
	}
}

func BenchmarkMercenneTwister(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		benchmark.MercenneTwister()
	}
}
