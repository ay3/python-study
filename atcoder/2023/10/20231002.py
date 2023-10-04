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


# ABC088B - Card Game for Two
# https://atcoder.jp/contests/abs/tasks/abc088_b
n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
alice = 0
bob = 0

for i in range(len(a)):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)


# ABC085B - Kagami Mochi
# https://atcoder.jp/contests/abs/tasks/abc085_b
n = int(input())
d = [0] * n

for i in range(n):
    d[i] = int(input())
    
print(len(list(set(d))))
