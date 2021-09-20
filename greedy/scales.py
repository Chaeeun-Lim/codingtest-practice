import sys

N = int(sys.stdin.readline())
chu_list = list(map(int, sys.stdin.readline().split()))
chu_list.sort()

result = 0
for i in range(N):
    if result + 1 >= chu_list[i]:
        result += chu_list[i]
    else:
        break

print(result+1)