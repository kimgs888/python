import sys
from collections import deque
input = sys.stdin.readline
def bfs(v):
    q = deque()
    q.append(v)
    visited = [0]*n
    while q:
        now = q.popleft()
        for i in route[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    print(*visited)

n = int(input())
route = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        if lst[j] == 1:
            route[i].append(j)

for i in range(n):
    bfs(i)