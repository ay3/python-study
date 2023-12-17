# https://atcoder.jp/contests/abc333/tasks/abc333_b
# B - Pentagon

S = list(input())
T = list(input())
d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
ans = "No"

S_N = min(abs(d[S[0]] - d[S[1]]), 5 - abs(d[S[0]] - d[S[1]]))
T_N = min(abs(d[T[0]] - d[T[1]]), 5 - abs(d[T[0]] - d[T[1]]))

if S_N == T_N:
    ans = "Yes"

print(ans) 
