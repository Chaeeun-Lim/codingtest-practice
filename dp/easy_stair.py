n = int(input())

d = [[0 for _ in range(10)] for _ in range(101)]
for i in range(1, 10):
    d[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        a = 0
        b = 0
        if 0 <= j-1 <= 9:
            a = d[i-1][j-1]
        if 0 <= j+1 <= 9:
            b = d[i-1][j+1]
        d[i][j] = a + b
print(sum(d[n]) % 1000000000)