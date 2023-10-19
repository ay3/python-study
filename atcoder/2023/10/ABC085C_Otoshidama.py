# ABC085C - Otoshidama
# https://atcoder.jp/contests/abs/tasks/abc085_c
N, Y = map(int, input().split())
x = -1 # 10000
y = -1 #  5000
z = -1 #  1000
sum = 0

for i in range(N + 1):
    for j in range(N - i + 1):
        k = N - i - j
        sum = i * 10000 + j * 5000 + k * 1000
        if sum == Y:
            x, y, z = i, j, k
            break

print(x, y, z)
