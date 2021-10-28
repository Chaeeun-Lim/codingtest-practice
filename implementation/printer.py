import sys

case = int(sys.stdin.readline())
# 케이스의 수 만큼 반복한다
for _ in range(case):
    result = 1
    file_cnt, loc = map(int, sys.stdin.readline().split())
    file_list = list(map(int, sys.stdin.readline().split()))
    file_check = [0 for _ in range(file_cnt)]
    file_check[loc] = 1

    while True:
        max_file = max(file_list)
        # 가장 큰 파일이 맞다면
        if file_list[0] == max_file:
            if file_check[0] == 1:
                print(result)
                break
            else:
                del file_list[0]
                del file_check[0]
                result += 1
        # 아니라면
        else:
            file_list.append(file_list[0])
            file_check.append(file_check[0])
            del file_list[0]
            del file_check[0]
