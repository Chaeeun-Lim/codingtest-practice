#단어의 개수
n = int(input())
# 단어받기
words = list()
for _ in range(n):
    words.append(input())
# (알파벳, 숫자) 담는 사전
rs_dict = dict()
for i in words:
    # 단어의 길이-1
    leng = len(i)-1
    for j in range(leng+1):
        # j는 자리수임
        if i[j] in rs_dict:
            # 가지고 있음!
            rs_dict[i[j]] += int('1'+('0'*(leng-j)))
        else:
            # 없음!
            rs_dict[i[j]] = int('1'+('0'*(leng-j)))

# 큰값을 기준으로 정렬
sort_list = sorted(rs_dict.items(),key= lambda a:a[1], reverse=True)

# 큰거면서 9부터 곱해줌
num = 9
result = 0
for i in sort_list:
    result += i[1]*num
    num -= 1

print(result)