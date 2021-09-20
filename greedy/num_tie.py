# 입력받을 수
n = int(input())
# 수 담을 리스트
fin_list = list()
plus_list = list()
min_list = list()

for _ in range(n):
    num = int(input())
    if num == 1:
        fin_list.append(num)
    elif num <= 0:
        min_list.append(num)
    elif num > 1:
        plus_list.append(num)
# 오름차순정렬
min_list.sort(reverse=True)
plus_list.sort()

while True:
    if len(min_list) == 1:
        fin_list.append(min_list.pop())
        break
    if len(min_list) == 0:
        break

    a = min_list.pop()
    b = min_list.pop()
    fin_list.append(a*b)


while True:
    if len(plus_list) == 1:
        fin_list.append(plus_list.pop())
        break
    if len(plus_list) == 0:
        break

    a = plus_list.pop()
    b = plus_list.pop()
    fin_list.append(a * b)

print(sum(fin_list))

