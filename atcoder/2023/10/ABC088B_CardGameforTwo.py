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
