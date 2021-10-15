import sys
sys.setrecursionlimit(1000000)

result = []

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def dfs(x, y):
    if x<0 or x>=h or y<0 or y>=w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(9):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

while True:
    # 넓이와 높이를 입력받는다.
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    # 그래프 생성
    graph = []
    # 높이만큼 입력받기
    for _ in range(h):
        lst = list(map(int, sys.stdin.readline().split()))
        graph.append(lst)
    # dfs 검사
    for a in range(h):
        for b in range(w):
            if dfs(a, b) == True:
                cnt += 1
    result.append(cnt)

for c in result:
    print(c)