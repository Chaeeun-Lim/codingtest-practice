import heapq
import sys
# 카드의 개수와 카드 합체의 수 입력받음
n, m = map(int, sys.stdin.readline().split())

# 카드들을 입력받음
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

for i in range(m):
    # 더할 수 2개를 뽑음 - 우선순위 큐로 가장 작은 수 두개 뽑음
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    new = x + y
    heapq.heappush(cards, new)
    heapq.heappush(cards, new)

print(sum(cards))
