# 사람의 수
n = int(input())
# 인출시간
time_list = sorted(list(map(int, input().split())))
# 각 인출시간의 합계를 저장
total = 0
# 인출시간 합계 리스트
sum_list = list()

for i in time_list:
    total += i
    sum_list.append(total)

result = sum(sum_list)
print(result)
