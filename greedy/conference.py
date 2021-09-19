#회의의 개수 입력받기
n = int(input())
#회의의 수 만큼 튜플만들어서 리스트형태로 저장
cf_list = list()
#총 회의 수 담는 변수
cnt = 0
#현재 회의 끝나는 시간을 담고있는 변수
end = 0

for _ in range(n):
    s, e = map(int, input().split())
    cf = (s,e)
    cf_list.append(cf)
# 끝나는 시간이 작은거 부터 정렬하기 (끝나는 시간이 같다면 시작시간이 작은 것 부터)
cf_list = sorted(cf_list, key=lambda a:a[0])
cf_list = sorted(cf_list, key=lambda a:a[1])

for i in cf_list:
    #끝 시간을 비교한다
    #끝나는 시간이 내 시작시간보다 작거나 같으면 회의에 추가한다
    if end <= i[0]:
        cnt += 1
        #끝나는 시간을 i의 끝시간으로 변경
        end = i[1]
print(cnt)