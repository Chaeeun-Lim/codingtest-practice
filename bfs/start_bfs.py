# BFS(Breadth-First-Search) 너비 우선 탐색
'''
그래프에 가까운 노드부터 우선적으로 탐색하는 알고리즘
BFS는 큐 자료구조를 이용하며, 구체적인 동작과정은 다음과 같습니다.
    1. 탐색시작노드를 큐에 삽입하고 방문처리를 합니다.
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
        모두 큐에 삽입하고 방문처리 합니다.
    3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
'''
from collections import deque
# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐의 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드에 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 미로탈출문제
'''
아이디어
    BFS는 시작시점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색합니다.
    상하좌우로 연결된 모든 노드로의 거리가 1로 동일하다
        따라서 (1,1) 지점부터 bfs를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결가능`
'''
from collections import deque
# N, M을 공백 기준으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네가지의 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))