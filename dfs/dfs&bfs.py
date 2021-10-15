# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 번호 V
# 다음 M개 줄에는 간선이 연결하는 두 정점의 번호가 주어짐 간선은 양방향
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = list([] for i in range(n))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph[a-1]:
        graph[a-1].append(b)
    if a not in graph[b-1]:
        graph[b-1].append(a)

for i in graph:
    i.sort()

dfs_visited = [False] * n
bfs_visited = [False] * n

def dfs(graph, v, dfs_visited):
    # 현재 노드 방문처리
    dfs_visited[v-1] = True
    print(v, end=' ')
    for i in graph[v-1]:
        if not dfs_visited[i-1]:
            dfs_visited[i-1] = True
            dfs(graph, i, dfs_visited)

def bfs(graph, v, bfs_visited):
    queue = deque([v])
    bfs_visited[v-1] = True
    while queue:
        item = queue.popleft()
        print(item, end=' ')
        for i in graph[item-1]:
            if not bfs_visited[i-1]:
                queue.append(i)
                bfs_visited[i-1] = True

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)

