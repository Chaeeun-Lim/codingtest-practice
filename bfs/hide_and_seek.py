from collections import deque

n, m = map(int, input().split())
max = 10 ** 5
dist = [0] * (max+1)

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == m:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

bfs()