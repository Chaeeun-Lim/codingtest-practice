import sys
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def color_dfs(x, y, graph, color):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] != 'X' and graph[x][y] == color:
        graph[x][y] = 'X'
        for i in range(4):
            color_dfs(x+dx[i], y+dy[i], graph, color)
        return True
    return False

def dfs(x, y, graph):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] != 'X':
        color = graph[x][y]
        graph[x][y] = 'X'
        for i in range(4):
            color_dfs(x+dx[i], y+dy[i], graph, color)
        return True
    return False


n = int(sys.stdin.readline())
graphs = [[],[]]
for _ in range(n):
    lst = list(sys.stdin.readline().strip())
    graphs[0].append(lst)
    lst_1 = []
    for i in lst:
        if i == 'G':
            i = 'R'
        lst_1.append(i)
    graphs[1].append(lst_1)


for i in range(2):
    cnt = 0
    for j in range(n):
        for k in range(n):
            if dfs(j, k, graphs[i]) == True:
                cnt += 1
    print(cnt, end=' ')
