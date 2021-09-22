import sys
# 레벨수와 레벨당 스코어 입력받기
N = int(sys.stdin.readline())
scores = list()
for _ in range(N):
    score = int(sys.stdin.readline())
    scores.append(score)
# 거꾸로 바꾸기
scores.reverse()
# 레벨을 내린 횟수
cnt = 0
# 현재 점수
now = scores[0]
for i in range(1, N):
    diff = now - scores[i]
    if diff <= 0:
        cnt += -diff + 1
        now -= 1
    else:
        now = scores[i]

print(cnt)

