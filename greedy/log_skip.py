import sys

# 테스트 케이스 개수
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    logs = list(map(int, sys.stdin.readline().split()))
    logs.sort()
    max_diff = 0
    for i in range(2, N):
        max_diff = max(max_diff, abs(logs[i] - logs[i-2]))
    print(max_diff)




