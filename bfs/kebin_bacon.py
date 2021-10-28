import sys
from collections import deque

def bfs(graph, start):
    visited = [[False, 0] for _ in range(user + 1)]
    queue = deque()
    queue.append(start)
    sum = 0
    # 방문처리
    visited[start][0] = True
    # while 문 시작
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            # 방문하지 않은 노드에 대해서만
            if not visited[i][0]:
                # 방문처리, 관계수 더해주기
                visited[i][0] = True
                visited[i][1] = visited[x][1] + 1
                queue.append(i)
    # 다 끝나면 케빈 베이컨 수 더하기
    for j in visited:
        sum += j[1]
    return [start, sum]

user, relation = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(user+1)]
graph[0] = [0, 0]
result = []

for _ in range(relation):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

for i in range(1, user+1):
    res = bfs(graph, i)
    result.append(res)

answer = result[0]
for i in range(1, len(result)):
    if answer[1] > result[i][1]:
        answer[0] = result[i][0]
        answer[1] = result[i][1]
print(answer[0])
