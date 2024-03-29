def dfs(c,cnt):
    global result
    if result >= cnt*100:
        return
    if c == n:
        sumnum = round(cnt*100,6)
        result = max(result,sumnum)
        return

    for i in range(n):
        if not visited[i] and lst[c][i] != 0:
            visited[i] = 1
            dfs(c+1, cnt * (lst[c][i]/100))
            visited[i] = 0

for t in range(int(input().strip())):
    n = int(input().strip())
    lst = [list(map(int,input().strip().split())) for _ in range(n)]
    visited = [0] * (n+1)
    result = 0
    dfs(0,1)
    sumnum = f'{result:.6f}'
    print(f'#{t+1} {sumnum}')