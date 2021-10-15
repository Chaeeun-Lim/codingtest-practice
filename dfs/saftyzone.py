import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, standard):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<n and visited[nx][ny] == 0 and graph[nx][ny] > standard:
            visited[nx][ny] = 1
            dfs(nx, ny, standard)


n = int(sys.stdin.readline())

graph = []
maxi = 0
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    maxi = max(maxi, max(lst))
    graph.append(lst)

result = 0
for i in range(maxi):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j, k, i)
    result = max(result, cnt)

print(result)

