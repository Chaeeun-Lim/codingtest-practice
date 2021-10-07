import sys
# 자리수 N과 지울개수 K를 입력받음
N, K = map(int, sys.stdin.readline().split())
value = list(map(int, sys.stdin.readline().strip()))

stack = list()
del_num = K

for i in range(N):
    while del_num > 0 and stack:
        if stack[len(stack)-1] < value[i]:
            stack.pop()
            del_num -= 1
        else:
            break
    stack.append(value[i])

print(stack)

