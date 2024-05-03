package lcg_test

import (
	"testing"

	lcg "github.com/shunta0213/b3-a2-exp/src/scripts/linear-congruential-generator/go"
)

func TestLCG(t *testing.T) {
	lcg := lcg.NewLCG(0, 40, 181, 20040213)

	t.Run("Next", func(t *testing.T) {
		val := lcg.Next()
		t.Logf("Next: %d\n", val)
	})
}

func TestFindCycle(t *testing.T) {
	t.Run("FindCycle", func(t *testing.T) {

		l := lcg.NewLCG(0, 40, 181, 20040213)
		cycle := lcg.FindCycle(l)
		t.Logf("Cycle: %d\n", cycle)
	})

	t.Run("FindCycle kwnown", func(t *testing.T) {
		l := lcg.NewLCG(1, 13, 5, 12)
		cycle := lcg.FindCycle(l)

		if cycle != 12 {
			t.Errorf("Expected: 12, but got: %d\n", cycle)
		}
	})

	t.Run("Error Case", func(t *testing.T) {
		l := lcg.NewLCG(123456, 65520, 65459, 2147483765)
		cycle := lcg.FindCycle(l)
		t.Logf("Cycle: %d\n", cycle)
	})
}

// func FuzzLCG(f *testing.F) {
// 	logFile, err := os.OpenFile("lcg_fuzz_results.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
// 	if err != nil {
// 		f.Errorf("Error opening file: %s\n", err)
// 		return
// 	}
// 	defer logFile.Close()

// 	f.Add(uint64(573180), uint64(65536), uint64(65536), uint64(1474838))
// 	f.Add(uint64(420211), uint64(53011), uint64(47301), uint64(3784138))

// 	f.Fuzz(func(t *testing.T, seed uint64, a uint64, c uint64, m uint64) {
// 		if a >= m || c >= m {
// 			t.Skip()
// 		}

// 		l := lcg.NewLCG(seed, a, c, m)
// 		cycle := lcg.FindCycle(l)
// 		t.Logf("Cycle: %d\n", cycle)
// 		if cycle > 10 {
// 			result := fmt.Sprintf("%v, %v, %v, %v, %v\n", seed, a, c, m, cycle)
// 			if _, err := logFile.WriteString(result); err != nil {
// 				t.Errorf("Failed to write to log file: %s", err)
// 			}
// 		}
// 	})
// }
