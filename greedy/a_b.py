A, B = map(int, input().split())
cnt = 0

while B > 0:
    if B == A:
        break
    # 짝수인 경우
    if B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        B = int(round(B * 0.1))
        cnt += 1

print(cnt+1 if A == B else -1)
