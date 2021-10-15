import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 0:
                cnt += 1
                graph[nx][ny] = 2
                queue.append((nx, ny))
    result.append(cnt)
    print(graph)

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    p, q, x, y = map(int, sys.stdin.readline().split())
    start = (q, p)
    end = (y, x)
    for i in range(q, y):
        for j in range(p, x):
            if graph[i][j] == 0:
                graph[i][j] = 1
print(graph)
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(i,j)
            graph[i][j] = 2
            bfs(i, j)
