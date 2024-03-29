def dfs(battery,r,cnt):
    global result
    if result<cnt:
        return
    if battery == 0:
        return
    if n == r:
        result = min(result,cnt)
        return

    dfs(battery-1,r+1,cnt)
    dfs(data[r],r+1,cnt+1)


for t in range(int(input())):
    data = list(map(int,input().split()))
    n = data[0]
    result = float('inf')
    dfs(data[1],2,0)
    print(f'#{t+1} {result}')