n = int(input())

if n == 1 or n == 3:
    print(-1)
elif n % 5 == 0:
    print(n//5)
else:
    q, d = divmod(n, 5)
    if d % 2 == 0:
        print(q+(d//2))
    else:
        q -= 1
        d += 5
        print(q+(d//2))