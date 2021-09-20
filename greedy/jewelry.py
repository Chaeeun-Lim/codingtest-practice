import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
# 보석리스트 (무게, 가격) 튜플을 담음
jw_list = list()
# 가방 리스트
bag_list = list()

for _ in range(N):
    # 무게가 가벼운순으로 힙push
    li = list(map(int, input().split()))
    heapq.heappush(jw_list, li)

for _ in range(K):
    bag_list.append(int(input()))
bag_list.sort()

# 총 훔친금액
total_price = 0
# 주얼리 후보들
candidate = list()

for bag in bag_list:
    while jw_list and bag >= jw_list[0][0]:
        M, V = heapq.heappop(jw_list)
        heapq.heappush(candidate, -V)
    if candidate:
        total_price += -heapq.heappop(candidate)

print(total_price)
