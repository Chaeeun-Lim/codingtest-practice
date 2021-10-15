import sys
from collections import deque
sys.setrecursionlimit(1000000)

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1<nx<n and -1<ny<m and -1<nz<h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

cnt = 0
result = -2

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                cnt = 1
            result = max(result, graph[i][j][k])

if cnt == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
