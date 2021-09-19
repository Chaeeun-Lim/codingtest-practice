# 산 물건 가격
n = int(input())
# 잔돈 리스트
change_list = [500,100,50,10,5,1]
# 잔돈으로 주어야할 돈
change = 1000-n
# 잔돈 개수
cnt = 0

for i in change_list:
    if i > change:
        continue
    else:
        cnt += change//i
        change %= i

print(cnt)