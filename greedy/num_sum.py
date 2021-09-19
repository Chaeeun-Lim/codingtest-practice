s = int(input())
i = 1
cnt = 0
while s > 0:
    if s-i < i+1:
        cnt += 1
        break
    s -= i
    cnt += 1
    i += 1

print(cnt)