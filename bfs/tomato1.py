import sys
from collections import deque
sys.setrecursionlimit(1000000)

# 가로와 세로
m, n = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

def bfs():
    # 큐가빌떄까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

# 1인것들 집어넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

# bfs실행
bfs()

# 결과보기
cnt = 0
result = -2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt = 1
        result = max(result, graph[i][j])

if cnt == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)