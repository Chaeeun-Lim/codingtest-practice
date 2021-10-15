import sys

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
graph[0] = [0, 0]
visited = [False for _ in range(n+1)]

cnt = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

def dfs(graph, start, visited):
    # 현재노드 방문처리
    visited[start] = True
    # 현재노드와 연결된 다른 노드들을 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

for j in range(1, len(visited)):
    if not visited[j]:
        cnt += 1
        dfs(graph, j, visited)

print(cnt)
