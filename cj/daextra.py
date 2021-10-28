import sys
# 무한을 의미
INF = int(1e9)
# 노드의 수 간선의 수 입력
n, m = map(int, input().split())
# 시작노드 입력받기
start = int(input())
# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한적 있는지 체크하는 리스트
visited = [False] * (n+1)
# 최단거리테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단거리가 짧은 노드를 반환
def get_smallest_node():
    min_value = INF
    # 가장 최단거리가 짧은 노드
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    # 연결되어있는 노드 중
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작노드를 제외한 전체 n-1개 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 환인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거처 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기위한 최단거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 False 출력
    if distance[i] == INF:
        print(False)
    else:
        print(distance[i])