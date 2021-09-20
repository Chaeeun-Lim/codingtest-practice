# N M값 입력받음
N, M = map(int, input().split())

# 행렬 A, B 입력받음
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

# 변경한 횟수
cnt = 0

# 두 행렬이 같은지 비교하는 함수
def isEqual(a, b):
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

# 행렬의 위치를 바꾸는 함수
def change_position(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

# 두 함수를 비교해서 같은지 확인하자
for i in range(0, N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
            change_position(i ,j)
            cnt += 1

print(cnt if isEqual(A, B) else -1)