# 주유소 개수
n = int(input())
# 거리
dis_list = list(map(int, input().split()))
# 오일값
price_list = list(map(int, input().split()))
# (오일, 거리값) 튜플 담을 list()
tup_list = list()
#(오일, 거리값)으로 튜플 생성
for i in range(n-1):
    tup_list.append((price_list[i],dis_list[i]))

# 비교해서 총 금액 구하기
price = tup_list[0][0] * tup_list[0][1]
now_price = tup_list[0][0]
for i in range(1,n-1):
    if tup_list[i][0] > now_price:
        price += now_price * tup_list[i][1]
    else:
        now_price = tup_list[i][0]
        price += now_price * tup_list[i][1]

print(price)