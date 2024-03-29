def dfs(c,cnt):
    global result
    if result <= cnt:
        return
    if c == n:
        result = min(result,cnt)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(c+1, cnt + lst[c][i])
            visited[i] = 0

for t in range(int(input().strip())):
    n = int(input().strip())
    lst = [list(map(int,input().strip().split())) for _ in range(n)]
    visited = [0] * (n+1)
    result = float('inf')
    dfs(0,0)
    print(f'#{t+1} {result}')