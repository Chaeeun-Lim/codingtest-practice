import sys
from collections import deque
sys.setrecursionlimit(1000000)
# 컴퓨터의 수
n = int(sys.stdin.readline())
# 컴퓨터 쌍의 수
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
graph[0] = [0, 0]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

visited = [False]*(n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재노드 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
cnt = 0
for i in visited:
    if i == True:
        cnt += 1
print(cnt-1)
