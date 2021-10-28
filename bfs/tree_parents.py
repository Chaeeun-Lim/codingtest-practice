import sys
from collections import deque
sys.setrecursionlimit(10000000)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
graph[0] = [0, 0]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (n+1)
result = []
for i in range(1, n+1):
    result.append([i, 0])

def dfs(graph, start, visited):
    # 우선 현재 노드를 방문처리한다
    visited[start] = True
    # 현재 노드에 연결된 것들 탐색하기
    for i in graph[start]:
        # 방문 안한것들은
        if not visited[i]:
            result[i-1][1] = start
            # 재귀호출
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                result[i-1][1] = x
                visited[i] = True
                queue.append(i)


bfs(graph, 1, visited)

for i in range(1, len(result)):
    print(result[i][1])
