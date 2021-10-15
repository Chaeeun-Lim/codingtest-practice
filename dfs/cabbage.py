# 입력받기
import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fin = []

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

t = int(sys.stdin.readline())
# 테스트케이스 수만큼 반복
for _ in range(t):
    result = 0
    m, n, k = map(int, sys.stdin.readline().split())
    # k그래프 입력받기
    graph = [[0]*m for i in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    for a in range(n):
        for b in range(m):
            if dfs(a, b) == True:
                result += 1
    fin.append(result)

for c in fin:
    print(c)