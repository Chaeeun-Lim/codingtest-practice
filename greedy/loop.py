# 로프의 개수
n = int(input())
# 각 로프의 중량
weight_list = list()
for _ in range(n):
    weg = int(input())
    weight_list.append(weg)
# 내림차순 정렬
weight_list = sorted(weight_list, reverse=True)

# 최대하중 구하기
max_weight = 0
for i in range(len(weight_list)):
    if max_weight <= (i+1)*weight_list[i]:
        max_weight = (i+1)*weight_list[i]

# 최댓갑 출력
print(max_weight)