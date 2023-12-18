# https://atcoder.jp/contests/abc333
# C - Repunit Trio

N = int(input())
R = []
A = []
for i in range(1, 13):
    a = int("1" * i)
    R.append(a)

for i in range(len(R)):
    for j in range(len(R)):
        for k in range(len(R)):
            a = R[i] + R[j] + R[k]
            if a not in A:
                A.append(a)

A.sort()
print(A[N - 1])
