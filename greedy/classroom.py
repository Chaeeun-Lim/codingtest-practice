import heapq
import sys

# 수업의 수와 시작시간과 종료시간 입력받자
N = int(sys.stdin.readline())
classes = list()
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    classes.append([S, T])
classes .sort()

# 수업이 끝나는 시작과 다음 수업이 시작하는 시간이 중요하다
# 우선순위 큐로 끝나는 시간을 관리
rooms = list()
heapq.heappush(rooms, classes[0][1])

for i in range(1, N):
    if classes[i][0] < rooms[0]:
        heapq.heappush(rooms, classes[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, classes[i][1])

print(len(rooms))