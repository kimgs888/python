import sys
input = sys.stdin.readline
from collections import deque
def bfs(v):
    q = deque()
    hide = f'{v}'
    q.append([v,hide])
    visited[v] = 0
    while 1:
        now,route = q.popleft()
        if now == k:
            return route
        calculate = [now + 1, now - 1, now * 2]
        for i in range(3):
            if 0<=calculate[i]<=100000 and not visited[calculate[i]]:
                newroute = route + '_' + f'{calculate[i]}'
                visited[calculate[i]] = visited[now] + 1
                q.append([calculate[i],newroute])

n,k = map(int,input().strip().split())
visited = [0] * 100001
answer = bfs(n)
ans = answer.split('_')
print(len(ans)-1)
print(' '.join(ans))
