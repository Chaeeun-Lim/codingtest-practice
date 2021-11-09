import re
import math

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    A, B = [], []
    for i in range(1, len(str1)):
        s = str1[i-1]+str1[i]
        if re.match('[A-Z]', s[0]) and re.match('[A-Z]', s[1]):
            A.append(s)
    for i in range(1, len(str2)):
        s = str2[i-1]+str2[i]
        if re.match('[A-Z]', s[0]) and re.match('[A-Z]', s[1]):
            B.append(s)
    inter, union = 0, 0
    if not A and not B:
        return 65536
    while A:
        a = A.pop()
        if a in B:
            inter += 1
            union += 1
            i = B.index(a)
            del B[i]
        else:
            union += 1
    return int((inter / (union+len(B))*65536))

def a_solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    inter = set(str1) & set(str2)
    union = set(str1) | set(str2)

    if len(union) == 0:
        return 65536

    inter_sum = sum([min(str1.count(i), str2.count(i)) for i in inter])
    union_sum = sum([max(str1.count(u), str2.count(u)) for u in union])

    return math.floor((inter_sum/union_sum)*65536)

def self(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    inter = set(str1) & set(str2)
    union = set(str1) | set(str2)

    if len(union) == 0:
        return 65536

    inter_sum = sum([min(str1.count(i), str2.count(i)) for i in inter])
    union_sum = sum([max(str1.count(u), str2.count(u)) for u in union])

    return math.floor((inter_sum/union_sum)*65536)

str1, str2 = 'E=M*C^2', 'e=m*c^2'
str11, str22 = 'aa1+aa2', 'AAAA12'
print(self('FRANCE', 'french'))
print(self(str1, str2))
print(self(str11, str22))