# 문장과 키워드 입력받기
str = input()
keyw = input()
# 나오는 수
cnt = 0

while True:
    if str.find(keyw) == -1:
        break
    cnt += 1
    index = str.find(keyw) + len(keyw)
    str = str[index:]

print(cnt)

