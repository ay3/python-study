# ABC085B - Kagami Mochi
# https://atcoder.jp/contests/abs/tasks/abc085_b
n = int(input())
d = [0] * n

for i in range(n):
    d[i] = int(input())
    
print(len(list(set(d))))
