import sys

n = int(sys.stdin.readline())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j-1 < 0 or j-1 >= len(triangle[i-1]):
            triangle[i][j] += triangle[i-1][j]
        elif j < 0 or j >= len(triangle[i-1]):
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[n-1]))