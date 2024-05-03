package benchmark

import (
	cryptorand "crypto/rand"
	"math/big"
	mathrand "math/rand"

	"github.com/seehuhn/mt19937"
)

const (
	modulo = 2 ^ 16 + 1
	a      = 75
	c      = 74
	seed   = 1
)

func MathRand() uint64 {
	return mathrand.Uint64()
}

func CryptoRand() uint64 {
	n, _ := cryptorand.Int(cryptorand.Reader, big.NewInt(2^63))
	return n.Uint64()
}

func LCG() uint64 {
	return (a*seed + c) % modulo
}

func MercenneTwister() int64 {
	return mt19937.New().Int63()
}
