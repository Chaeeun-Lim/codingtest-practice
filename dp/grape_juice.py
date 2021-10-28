import sys

n = int(sys.stdin.readline())
j = [0]
for _ in range(n):
    j.append(int(sys.stdin.readline()))

d = [0] * (n+1)
d[1] = j[1]
if n > 1:
    d[2] = j[1] + j[2]

for i in range(3, n+1):
    d[i] = max(d[i-3]+j[i-1]+j[i], d[i-2]+j[i], d[i-1])

print(d[n])