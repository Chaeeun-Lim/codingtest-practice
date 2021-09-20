# 튜플 쌍을 저장할 리스트
tup_list = list()

# l p v 가 모두 0이 나올 때 까지 입력을 받음
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    tup_list.append((l, p, v))

for i in range(len(tup_list)):
    val = tup_list[i][2] // tup_list[i][1]
    remain = tup_list[i][2] % tup_list[i][1]
    result = (val * tup_list[i][0]) + min(tup_list[i][0], remain)
    print('Case %d: %d' %(i+1, result))

