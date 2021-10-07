import sys

T = int(sys.stdin.readline())
for _ in range(T):
    one = 0
    zero = 0
    N, M = sys.stdin.readline().split()
    for i in range(len(N)):
        if N[i] != M[i]:
            if N[i] == '0':
                zero += 1
            else:
                one += 1
    result = min(zero, one) + abs(zero - one)
    print(result)


