import sys

N = int(sys.stdin.readline())
books = list()
cnt = 0
for _ in range(N):
    book = int(sys.stdin.readline())
    books.append(book)
b_max = books[0]
for i in range(1, N):
    if books[i] > b_max:
        if b_max+1 != books[i]:
            cnt += 1
        b_max = books[i]

    else:
        cnt += 1
print(cnt)