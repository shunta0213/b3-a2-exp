#include <stdio.h>
#include <stdlib.h>
#include <search.h>
#include <stdint.h>

#define A 1664525
#define C 1013904223
#define M 4294967296
#define SEED 123456

int main()
{
    unsigned long long x = SEED;
    unsigned long long current_value = (A * x + C) % M;
    int count = 0;
    ENTRY e, *ep;

    hcreate(M); // ハッシュテーブルの作成

    // 初期値の設定
    e.key = malloc(20);                    // 文字列キー用のメモリ割り当て
    sprintf(e.key, "%llu", current_value); // 数値を文字列に変換
    e.data = (void *)(intptr_t)1;
    hsearch(e, ENTER);

    while (1)
    {
        current_value = (A * current_value + C) % M;
        count++;

        char *new_key = malloc(20);              // 新しいキー用のメモリ割り当て
        sprintf(new_key, "%llu", current_value); // 更新された数値を文字列に変換
        e.key = new_key;
        ep = hsearch(e, FIND); // 既存の値を検索
        if (ep)
        {
            // 周期発見
            printf("Period detected: %d iterations\n", count);
            free(new_key); // 新しいキーのメモリを解放（不要な場合）
            break;
        }
        else
        {
            // 新規値をハッシュテーブルに追加
            e.data = (void *)(intptr_t)(count + 1);
            hsearch(e, ENTER);
        }

        if (count == M)
        {                  // 安全のための上限
            free(new_key); // 新しいキーのメモリを解放
            printf("No repetition within %llu iterations.\n", M);
            break;
        }
    }

    hdestroy(); // ハッシュテーブルの破棄
    return 0;
}
