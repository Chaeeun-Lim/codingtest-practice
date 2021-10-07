import sys

A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
channels = []
for _ in range(N):
    cha = int(sys.stdin.readline())
    channels.append(cha)

idx = 0
val = abs(B - channels[0])

for i in range(1, N):
    diff = abs(B - channels[i])
    # 차이가 더 작으면
    if diff < val:
        idx = i
        val = diff

if abs(B-A) <= val:
    print(abs(B-A))
else:
    print(1+val)

