import sys

n = int(sys.stdin.readline())
line = []
for _ in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))

line.sort(key=lambda a: a[0])
f = []
for l in line:
    f.append(l[1])

d = [1] * n
for i in range(1, n):
    for j in range(i):
        if f[i] > f[j]:
            d[i] = max(d[i], d[j]+1)

print(n-max(d))
