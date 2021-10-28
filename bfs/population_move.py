import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, visited):
    global is_move
    queue = deque()
    queue.append((x, y))
    zone_cnt = 1
    zone_sum = graph[x][y]
    zone_list = [[x, y]]
    visited[x][y] = True
    while queue:
        q_x, q_y = queue.popleft()
        for i in range(4):
            nx = q_x + dx[i]
            ny = q_y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(graph[q_x][q_y] - graph[nx][ny]) <=R:
                visited[nx][ny] = True
                zone_cnt += 1
                zone_sum += graph[nx][ny]
                zone_list.append([nx, ny])
                queue.append((nx, ny))
    average = zone_sum // zone_cnt
    if zone_cnt > 1:
        is_move = True
        for zone in zone_list:
            graph[zone[0]][zone[1]] = average


N, L, R = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = 0
while True:
    is_move = False
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, graph, visited)
    if is_move:
        result += 1
    else:
        break
print(result)