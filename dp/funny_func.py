w_dict = dict()
def w(a, b, c):
    global w_dict
    if (a, b, c) in w_dict:
        return w_dict[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        w_dict[(a, b, c)] = 1
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b < c:
        w_dict[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w_dict[(a, b, c)]
    w_dict[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return w_dict[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')