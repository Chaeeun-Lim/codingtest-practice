# 단지번호 붙이기
import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# 정답
result = []
# 단지의 개수
cnt = 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 함수 정의하기
def dfs(x, y):
    global cnt
    # 범위에서 벗어난 경우
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 방문하지 않은 경우
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        # 상하좌우 재귀호출
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False

for a in range(n):
    for b in range(n):
        if dfs(a, b) == True:
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for j in result:
    print(j)