t = int(input())

for _ in range(t):
    n = int(input())
    zero = 1
    one = 0
    for _ in range(n):
        result = one
        one = one + zero
        zero = result
    print(zero, one)

    n0 = [0]*41
    n1 = [0]*41
    n0[0], n1[1] = 1, 1
    for i in range(2, n+1):
        n0[i] = n0[i-1] + n0[i-2]
        n1[i] = n1[i-1] + n1[i-2]
    print(n0[n], n1[n])