def dfs(v,topheght):
    global result
    if topheght>result:
        return
    if v == n:
        if 0<=topheght:
            result = min(topheght,result)
        return
    for i in range(2):
        newtopheght = topheght + lst[v]*i
        dfs(v+1,newtopheght)
        newtopheght = topheght - lst[v]*i

for t in range(int(input())):
    n,b = map(int,input().split())
    lst = list(map(int,input().split()))
    result = float('inf')
    dfs(0,-b)
    print(f'#{t+1} {result}')