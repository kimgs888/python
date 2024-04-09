import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    visited[v] = 0
    q.append(v)
    while q:
        now = q.popleft()
        # if visited[now] == k:
        #     return
        for next in road[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)


n,m,k,x = map(int,input().split())
road = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for i in range(m):
    s,e = map(int,input().split())
    road[s].append(e)
bfs(x)
if k in visited:
    for i in range(len(visited)):
        if k == visited[i]:
            print(i)
else:
    print(-1)
