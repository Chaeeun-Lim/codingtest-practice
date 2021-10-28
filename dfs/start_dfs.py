# DFS(Depth-First-Search)
'''
DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘 입니다.
DFS는 스택자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
    1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 합니다.
    2. 스택에 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리 합니다.
        방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
    3. 더이상 2번의 과정을 수행할 수 없을 때 까지 반복합니다.
'''
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드들을 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 일반적으로 그래프는 노드의 번호가 1번부터 사용되는 경우가 많기 때문에 0번 인덱스는 비워둠
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
print(visited)

# 정의된 DFS함수 호출
dfs(graph, 1, visited)

# 얼음틀 문제
'''
아이디어 
    1. 특정한 지점의 상하좌우를 살펴본 뒤에 주변지점 중 값이 '0'이며 아직 방문하지 않은 특정지점이 있다면 해당 지점을 방문
    2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하는 과정을 반복하면 연결된 모든 지점 방문가능
    3. 모든 노드에 대해서 1-2번 과정을 반복하며 방분하지 않은 지점의 수를 카운트 
'''
# N, M을 공백 기준으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs_ice(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상하좌우의 위치들도 모두 재귀적으로 호출
        dfs_ice(x-1, y)
        dfs_ice(x, y-1)
        dfs_ice(x+1, y)
        dfs_ice(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs_ice(i, j) == True:
            result += 1

print(result)