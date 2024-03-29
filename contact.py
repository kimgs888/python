from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        now = q.popleft()

        for i in student[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)

for t in range(10):
    length, start = map(int,input().split())
    lst = list(map(int,input().split()))
    student = [[] for _ in range(101)]
    visited = [0]*101
    for i in range(length//2):
        s,e = i*2,i*2+1
        student[lst[s]].append(lst[e])
    bfs(start)
    for i in range(100,0,-1):
        if visited[i] ==  max(visited):
            answer = i
            break
    print(f'#{t+1} {answer}')