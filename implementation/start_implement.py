# 구현 : 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 풀이를 떠올리가는 쉽지만 소스코드로 옯기기 어려운 문제
# 유형 : 알고리즘은 간단, but 코드는 길다 / 실수연산을 다루고 특정 소수점 자리까지 출력
#       문자열을 특정 기준이 따라 끊어 처리 / 적절한 라이브러리 찾아서 사용
import sys
'''
# 방향문제
n = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# 시간문제
n = int(sys.stdin.readline())
cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            #if '3' in str(j) or '3' in str(i) or '3' in str(k):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1
print(cnt)

# 왕실 나이트 문제
# 수평으로 두칸 수직으로 한칸 / 수직으로 두칸 수평으로 한칸
# 8*8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 행:1-8 열: a-h
position = input()
row = int(position[1])
col = int(ord(position[0])) - int(ord('a')) + 1
'''
'''
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(len(alpa)):
    if position[0] == alpa[i]:
        col = i+1
'''
'''

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

answer = 0
for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]
    if 0<nx<9 and 0<ny<9:
        answer += 1
print(answer)

'''
# 문자열 재정렬
S = input()
char_list = []
sum = 0

for i in S:
    if i.isalpha():
        char_list.append(i)
    else:
        sum += int(i)
char_list.sort()

if sum != 0:
    char_list.append(str(sum))
print(''.join(char_list))
