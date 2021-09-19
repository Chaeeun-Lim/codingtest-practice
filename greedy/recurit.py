import sys
# 테스트케이스의 수 입력받음
n = int(input())
# 2중 for문을 돌려서 입력을 받음
for _ in range(n):
    # 하나의 테스트 케이스의 사원수
    num = int(input())
    # 하나의 테스트 케이스를 담을 리스트
    test_list = list()
    for i in range(num):
        a, b = map(int, sys.stdin.readline().split())
        test_list.append((a,b))
    # 뒤처지는지 검사
    test_list.sort()
    # 신입사원수 서류1등은 무조건 합격
    cnt = 1
    # 면접점수 서류1등의 면접점수
    score = test_list[0][1]
    for i in range(1,num):
        if test_list[i][1] < score:
            cnt += 1
            score = test_list[i][1]
    print(cnt)