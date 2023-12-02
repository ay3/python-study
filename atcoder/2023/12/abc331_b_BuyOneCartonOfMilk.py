# https://atcoder.jp/contests/abc331/tasks/abc331_b
# B - Buy One Carton of Milk

N, S, M, L = map(int, input().split())
max_S = N // 6 + 2  # S : 6
max_M = N // 8 + 2  # M : 8
max_L = N // 12 + 2 # L : 12

ans = max_S * S + max_M * M + max_L * L
sum = 0 # 合計の個数
price = 0 # 合計の金額

for i in range(max_S):
    for j in range(max_M):
        for k in range(max_L):
            sum = 6 * i + 8 * j + 12 * k
            if N <= sum:
                price = S * i + M * j + L * k
                ans = min(ans,price)

print(ans)
