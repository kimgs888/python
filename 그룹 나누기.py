def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        postion = q.pop(0)
        for i in student[postion]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

for t in range(int(input())):
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    student = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        s,e = i*2,i*2+1
        student[lst[s]].append(lst[e])
        student[lst[e]].append(lst[s])
    answer = 0
    for i in range(1,n+1):
        if not visited[i]:
            answer += 1
            bfs(i)
    print(f'#{t+1} {answer}')