# https://atcoder.jp/contests/abc331/tasks/abc331_b
# B - Buy One Carton of Milk

N, S, M, L = map(int, input().split())
a = (N + 6 - 1) // 6  # S : 6
b = (N + 8 - 1) // 8  # M : 8
c = (N + 12 - 1) // 12 # L : 12

ans = 1000000 # (10 ** 4) * 100
sum = 0 # 合計の個数
sum_m = 0 # 合計の金額

for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            sum = 6 * i + 8 * j + 12 * k
            if N <= sum:
                sum_m = S * i + M * j + L * k
                if sum_m <= ans:
                    ans = sum_m

print(ans)
