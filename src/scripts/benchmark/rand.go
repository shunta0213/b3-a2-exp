package benchmark

import (
	cryptorand "crypto/rand"
	"fmt"
	"math/big"
	mathrand "math/rand"
	"strconv"

	"github.com/seehuhn/mt19937"
)

var seed uint64 = 12345678

func MathRand() uint64 {
	return mathrand.Uint64()
}

func CryptoRand() uint64 {
	n, _ := cryptorand.Int(cryptorand.Reader, big.NewInt(2^63))
	return n.Uint64()
}

type LCG struct {
	seed   uint64
	a      uint64
	c      uint64
	modulo uint64
}

func NewLCG(seed uint64, a uint64, c uint64, modulo uint64) *LCG {
	return &LCG{
		seed:   seed,
		a:      a,
		c:      c,
		modulo: modulo,
	}
}

func (l *LCG) Gen() uint64 {
	l.seed = (l.a*l.seed + l.c) % l.modulo
	return l.seed
}

// generate 8 digits number
func MSM() uint64 {
	seedStr := fmt.Sprintf("%016d", seed)
	midSeedStr := seedStr[4:12]
	seed, _ = strconv.ParseUint(midSeedStr, 10, 64)
	return seed
}

func MercenneTwister() int64 {
	return mt19937.New().Int63()
}
