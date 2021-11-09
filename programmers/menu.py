from itertools import combinations
from collections import Counter

def solution(order, course):
    dict_list = []
    for _ in course:
        dict_list.append(dict())
    for i in range(len(order)):
        for j in range(len(course)):
            li = list(combinations(order[i], course[j]))
            for n in li:
                sn = tuple(sorted(n))
                if sn in dict_list[j]:
                    dict_list[j][sn] += 1
                else:
                    dict_list[j][sn] = 1
    answer = []
    for dic in dict_list:
        big = 2
        for d in dic:
            if dic[d] > big:
                big = dic[d]
        result = []
        for d in dic:
            if dic[d] == big:
                result.append(d)
        answer.append(result)
    ans = []
    for i in answer:
        for j in i:
            ans.append(''.join(j))
    ans.sort()
    return ans

def a_solution(orders, course):
    result = []
    for size in course:
        combi = []
        for order in orders:
            combi += combinations(sorted(order), size)

        most_order = Counter(combi).most_common()
        for k, v in most_order:
            if v > 1 and v == most_order[0][1]:
                result.append(''.join(k))
    result.sort()
    return result

def self(orders, courses):
    result = []
    for size in courses:
        combi = []
        for order in orders:
            combi += combinations(sorted(order), size)

        most_orders = Counter(combi).most_common()
        for k, v in most_orders:
            if v > 1 and v == most_orders[0][1]:
                result.append(''.join(k))
    result.sort()
    return result

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(self(orders, course))



