def bfs(v):
    q = []
    qidx = 0
    visited[v] = 0
    q.append(v)
    while q:
        now = q[qidx]
        if now == m:
            return visited[now]
        operateq = [now+1,now-1,now*2,now-10]
        for i in range(4):
            if 1<=operateq[i]<=10**6 and visited[operateq[i]]==0:
                visited[operateq[i]] = visited[now] + 1
                q.append(operateq[i])
        qidx += 1

for t in range(int(input())):
    n,m = map(int,input().split())
    visited = [0]*(10**6+1)
    result = bfs(n)
    print(f'#{t+1} {result}')