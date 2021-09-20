s = input()
change_cnt = 0
now = s[0]

for i in range(len(s)):
    if now == s[i]:
        pass
    else:
        now = s[i]
        change_cnt += 1

print(int(change_cnt/2) if (change_cnt % 2) == 0 else int(change_cnt//2)+1)


