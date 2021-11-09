import sys
import ast

t = int(sys.stdin.readline())

for _ in range(t):
    f = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip()[1:-1].split(",")))

    for i in range(len(f)):
        if f[i] == 'R':
            arr.reverse()
            if i == len(f)-1:
                print(arr)
                break
        else:
            if not arr:
                print("error")
                break
            else:
                del arr[0]
                if i == len(f) - 1:
                    print(arr)
                    break
