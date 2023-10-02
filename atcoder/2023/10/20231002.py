# ABC083B - Some Sums
# https://atcoder.jp/contests/abs/tasks/abc083_b
n, a, b = map(int, input().split())
answer = 0

for i in range(1, n + 1):
    sum = 0
    s = list(str(i))
    for j in range(len(s)):
        sum += int(s[j])
    if a <= sum and sum <= b:
        answer += i

print(answer)
