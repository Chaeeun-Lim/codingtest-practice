n = int(input())
num = list(map(int, input().split()))

d = [0]*n
d[0] = num[0]
for i in range(1, n):
    d[i] = max(num[i], d[i-1]+num[i])
print(max(d))