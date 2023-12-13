# https://atcoder.jp/contests/abc332/tasks/abc332_a
# A - Online Shopping

N, S, K = map(int, input().split())
sum = 0
for i in range(N):
    P, Q = map(int, input().split())
    sum += P * Q

if sum < S:
    sum += K
    
print(sum)
