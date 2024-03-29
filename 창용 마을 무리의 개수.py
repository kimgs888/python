from collections import deque

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in friend[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

for t in range(int(input())):
    n,m = map(int,input().split())
    friend = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in range(m):
        s,e = map(int,input().split())
        friend[s].append(e)
        friend[e].append(s)

    result = 0
    for i in range(1,n+1):
        if not visited[i]:
            bfs(i)
            result += 1


    print(f'#{t+1} {result}')