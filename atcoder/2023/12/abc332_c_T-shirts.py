# https://atcoder.jp/contests/abc332/tasks/abc332_c
# T-shirts

N, M = map(int, input().split())
S = input().split("0")
l_n = 0

for i in S:
    l_n = max(l_n, i.count("2"))
    if M < i.count("1"):
        l_n = max(l_n, i.count("2") + i.count("1") - M)
    
print(l_n)
