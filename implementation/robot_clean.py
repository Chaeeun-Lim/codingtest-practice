import sys
sys.setrecursionlimit(1000000)

# 북 동 서 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, d):
    global result
    # 청소 가능한 위치인지 확인
    if graph[x][y] == 0:
        # 청소해주기
        graph[x][y] = 2
        result += 1
    # 반시계 방향으로 돌면서 청소가능한 위치확인
    for _ in range(4):
        # 이동할 뱡항 위치 확인
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 그 위치가 청소 안되있는 경우, 청소하러 가고 종료
        if graph[nx][ny] == 0:
            move(nx, ny, nd)
            return
        # 청소되어있거나 벽일경우 방향바꾸기
        d = nd
    # 네면 다 청소되어있거나 벽이여서 이동하지 못한경우
    # 후진해서 청소가능한지 확인
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    # 만약 후진하는 곳이 벽이면 청소종료
    if graph[nx][ny] == 1:
        return
    # 아니면 방향유지 후진 후 청소 지속
    move(nx, ny, d)

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

move(x, y, d)
print(result)