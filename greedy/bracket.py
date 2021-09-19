# 식을 입력받는다 -기준으로 자름
str_list = input().split('-')

# 최종 리스트
rs_list = list()

for i in str_list:
    # +가 있으면 분할해서 정수로 만든다음 더하기
    if i.find('+'):
        li = i.split('+')
        sum = 0
        for j in li:
            sum += int(j)
        rs_list.append(sum)
    # 없으면 그냥 정수로 변경해서 리스트에 넣는다
    else:
        x = int(i)
        rs_list.append(x)
# - 해준다
result = 0
for i in range(0,len(rs_list)):
    if i == 0:
        result += rs_list[i]
    else:
        result -= rs_list[i]

print(result)