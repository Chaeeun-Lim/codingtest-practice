# 전체 동전의 개수 n과 총 금액 k 를 입력받음
n, k = map(int, input().split())
# 코인의 종류를 담을 리스트를 만듬
coin_list = list()
# 코인의 개수 담을
cnt = 0

# n의 수 만큼 반복하여 coin담기
for i in range(n):
    coin = int(input())
    coin_list.append(coin)

# 내림차순으로 코인정렬
coin_list = sorted(coin_list, reverse=True)
for i in coin_list:
    # 코인이 k보다 작으면 그냥 넘어감
    if k < i:
        continue
    cnt += k // i
    k %= i
    if k == 0:
        break

print(cnt)

