package lcg

type LCG struct {
	seed uint64 // 現在のシード値
	a    uint64 // 乗数
	c    uint64 // 加数
	m    uint64 // モジュラス
}

// NewLCGは新しいLCGジェネレータを作成
func NewLCG(seed, a, c, m uint64) *LCG {
	return &LCG{
		seed: seed,
		a:    a,
		c:    c,
		m:    m,
	}
}

// Nextは次の乱数を生成し、シードを更新
func (lcg *LCG) Next() uint64 {
	lcg.seed = (lcg.a*lcg.seed + lcg.c) % lcg.m
	return lcg.seed
}

func FindCycle(lcg *LCG) int {
	seen := make(map[uint64]int)
	count := 0

	for {
		val := lcg.Next()
		if pos, exists := seen[val]; exists {
			return count - pos // 周期を返す
		}
		seen[val] = count
		count++

		if lcg.m < uint64(count) {
			return -1
		}
	}
}
