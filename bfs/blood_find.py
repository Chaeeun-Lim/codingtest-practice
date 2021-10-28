import sys
from collections import deque
sys.setrecursionlimit(1000000)

def bfs(graph, com_x, com_y, visited):
    global result
    queue = deque()
    queue.append(com_x)

    while queue:
        start = queue.popleft()
        # 꺼낸거 방문처리
        visited[start][0] = True
        for i in graph[start]:
            # 방문 안한 노드에 한해서
            if not visited[i][0]:
                # 거리 입력하기
                visited[i][1] = visited[start][1] + 1
                if i == com_y:
                    result = visited[i][1]
                else:
                    queue.append(i)


def dfs(graph, com_x, com_y, visited):
    global result
    # 방문처리 해주고
    visited[com_x][0] = True
    # 연결된 노드들 중에
    for i in graph[com_x]:
        # 방문 안한 노드들만
        if not visited[i][0]:
            # 촌 수 더해주기
            visited[i][1] = visited[com_x][1] + 1
            # 도착했다면
            if i == com_y:
                result = visited[i][1]
            else:
                dfs(graph, i, com_y, visited)

people_cnt = int(sys.stdin.readline())
p_x, p_y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
result = -1

visited = [[False, 0] for _ in range(people_cnt+1)]
graph = [[] for _ in range(people_cnt+1)]
graph[0] = [0, 0]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

bfs(graph, p_x, p_y, visited)
print(result)