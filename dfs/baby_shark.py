import sys
from collections import deque

# 우선순위에 따라 탐색위치 조정
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs():
    global shark_eat, fist_count, shark_size
    # 상어의 위치와 먹이를 담을 리스트
    start = [(shark_x, shark_y)]
    # 이동을 담을 큐
    queue = deque()
    times = 0

    while start:
        p = start.pop()
        visited = [[0]*n for _ in range(n)]
        # 상어위치 방문표기
        visited[p[0]][p[1]] = 1
        size = 1
        # 처음 상어의 위치로부터 출발하므로 이동을 담는 리스트에 넣어줌
        queue.append(p)
        # 먹을 수 있는 물고기가 없으면 종료
        if fist_count == 0:
            break
        # 이동이 더이상 불가능할떄까지
        while queue:
            for _ in range(size):
                q = queue.popleft()
                for i in range(4):
                    nx = q[0] + dx[i]
                    ny = q[1] + dy[i]
                    # 좌표안에 들어오고 방문 안한 경우에 대해서
                    if -1<nx<n and -1<ny<n and visited[nx][ny] == 0:
                        # 바다이거나 동일한 크기의 물고기일 경우에만 이동가능하므로
                        if sea[nx][ny] == shark_size or sea[nx][ny] == 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = visited[q[0]][q[1]] + 1
                        elif sea[nx][ny] != 0 and shark_size > sea[nx][ny]:
                            # 먹을수 있는 먹이는 start에 담아준다
                            start.append((nx, ny))
                            visited[nx][ny] = visited[q[0]][q[1]] + 1
            if len(start):
                # start값이 존재하면 먹을 수 있는 먹이 중 가장 가까운 값을 찾음
                sx = start[0][0]
                sy = start[0][1]
                # for문을 돌면서 가장 가까운 거리에 있는 값 찾기
                for x, y in start:
                    if x < sx:
                        sx = x
                        sy = y
                    elif x == sx and y < sy:
                        sx = x
                        sy = y
                # 상어가 하나 먹음
                shark_eat += 1
                # 사이즈 업데이트
                if shark_eat == shark_size:
                    shark_size += 1
                    shark_eat = 0
                # 처음 상어가 있는 위치 초기화하고 위치 옮기기
                sea[p[0]][p[1]] = 0
                sea[sx][sy] = 9

                queue = deque()
                fist_count -= 1
                # 거리 저장
                times += visited[sx][sy] -1
                start = [(sx, sy)]
                # 먹이를 먹은경우 바로 위치 업데이트 되므로 바로 빠져나오기
                break
            size = len(queue)
    return times

n = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark_x = 0
shark_y = 0
fist_count = 0

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark_x = i
            shark_y = j
        elif sea[i][j] != 0:
            fist_count += 1

shark_size = 2
shark_eat = 0

print(bfs())