def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i] = s[i][0].upper() + s[i][1:].lower()
    return s


def solution1(s):

    return s.lower().title()


print(solution1("3people unFollowed me"))