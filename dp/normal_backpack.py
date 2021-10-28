import sys

n, k = map(int, sys.stdin.readline().split())
bp = [[0, 0]]
for _ in range(n):
    bp.append(list(map(int, sys.stdin.readline().split())))

d = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bp[i][0]
        v = bp[i][1]
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], v + d[i-1][j-w])

print(d[n][k])