import sys
# 과제 입력받기
N = int(sys.stdin.readline())
tasks = []
for _ in range(N):
    task = list(map(int, sys.stdin.readline().split()))
    tasks.append(task)

tasks.sort(key=lambda a: (a[0],a[1]), reverse=True)

i = tasks[0][0]
sum = 0
while i > 0:
    able = []
    for j in range(len(tasks)):
        if tasks[j][0] >= i:
            able.append([j, tasks[j][1]])
    if able:
        del_idx = 0
        for a in able:
            if a[1] > able[del_idx][1]:
                del_idx = a[0]
        sum += tasks[del_idx][1]
        tasks.pop(del_idx)
    i -= 1

print(sum)