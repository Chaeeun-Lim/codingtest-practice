import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
graph = []
for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[[0]*2 for _ in range(col)] for _ in range(row)]
    visited[0][0][1] = 1
    queue = deque()
    queue.append([0, 0, 1])
    while queue:
        x, y, isBreak = queue.popleft()
        if x == row-1 and y == col-1:
            return visited[x][y][isBreak]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<row and -1<ny<col:
                if graph[nx][ny] == 1 and isBreak == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][isBreak] == 0:
                    visited[nx][ny][isBreak] = visited[x][y][isBreak] + 1
                    queue.append([nx, ny, isBreak])
    return -1

print(bfs())