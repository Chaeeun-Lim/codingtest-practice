import sys
'''
n, m = map(int, sys.stdin.readline().split())
chicken_list = []
house_list = []
for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if li[j] == 1:
            house_list.append((i+1, j+1))
        elif li[j] == 2:
            chicken_list.append((i+1, j+1))
'''
li = dict()
li['1'] = 1
li['3'] = 2
print('1' in li)