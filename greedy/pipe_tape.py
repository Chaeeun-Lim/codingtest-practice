# 구멍개수, 테이프의 길이
N, L = map(int, input().split())
# 구멍 입력받기
holes = list(map(int, input().split()))
holes.sort()

# 테이프의 수 -> cnt+1 할때마다 테이프를 끊는다고 생각하자
cnt = 1
# 시작시점
start = holes[0]

for hole in holes:
    length = start + L - 1
    if hole <= length:
        continue
    else:
        start = hole
        cnt += 1

print(cnt)

