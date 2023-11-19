# https://atcoder.jp/contests/abc329
# https://atcoder.jp/contests/abc329/tasks/abc329_a
# B - Next
n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort(reverse=True)
print(a[1])
