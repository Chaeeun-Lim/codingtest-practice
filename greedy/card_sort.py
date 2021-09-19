# 카드묶음의 개수
import heapq

n = int(input())
# 카드묶음 리스트
cards = list()
for _ in range(n):
    cards.append(int(input()))
# 힙정렬
heapq.heapify(cards)

# 총 더한수를 저장할 변수
result = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a+b
    heapq.heappush(cards,a+b)

print(result)