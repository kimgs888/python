di = [1,0,-1,0]
dj = [0,1,0,-1]
def dfs(row,col,c,route):
    global result
    if move == c:
        result.add(route)
        return
    for i in range(4):
        crow,ccol = row+di[i], col+dj[i]
        if 0<=crow<n and 0<=ccol<n:
            dfs(crow,ccol,c+1,route + str(lst[crow][ccol]))

for t in range(int(input().strip())):
    n = 4
    move = 6
    lst = [list(map(int,input().strip().split())) for _ in range(n)]
    result = set()
    for i in range(n):
        for j in range(n):
            dfs(i,j,0,str(lst[i][j]))
    print(f'#{t+1} {len(result)}')