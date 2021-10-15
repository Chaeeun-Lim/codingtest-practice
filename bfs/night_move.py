import sys
from collections import deque

dx = [-2, -1, -2, -1, 1, 2, 1, 2]
dy = [-1, -2, 1, 2, -2, -1, 2, 1]
result = []

# bfs 함수 정의
def bfs(graph, start, end, h):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            result.append(graph[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= h:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    graph = [[0]*m for _ in range(m)]
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    bfs(graph, (a, b), (c, d), m)

for i in result:
    print(i)