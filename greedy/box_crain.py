import sys

# 크래인과 박스를 입력받는다
N = int(sys.stdin.readline())
crains = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
boxs = list(map(int, sys.stdin.readline().split()))
# 내립차순 정렬
crains.sort(reverse=True)
boxs.sort(reverse=True)

# 걸린 시간
cnt = 0

if max(boxs) > max(crains):
    print(-1)
else:
    while boxs:
        cnt += 1
        for crain in crains:
            if len(boxs) == 0:
                break
            # 지금 그 크레인이 집을 수 있는 최대 박스의 무게 선택
            for i in range(len(boxs)):
                if boxs[i] <= crain:
                    boxs.pop(i)
                    break
    print(cnt)