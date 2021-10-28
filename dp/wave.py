t = int(input())
d = [0] * 101
d[1], d[2], d[3] = 1, 1, 1
for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        d[i] = d[i-2] + d[i-3]
    print(d[n])
