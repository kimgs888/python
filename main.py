import sys
<<<<<<< HEAD
di,dj = [1,0,-1,0],[0,1,0,-1]
def dfs(r,c,tr,tc,position):
    global cnt
    if r == endrow-1 and c == endcol-1 and position + 1==m:
        cnt += 1
        return

    if r==tr and c == tc:
        newpos = position + 1
        ntr,ntc = stpt[newpos]
        dfs(r,c,ntr-1,ntc-1,newpos)

    for i in range(4):
        row = r + di[i]
        col = c + dj[i]
        if 0<=row<n and 0<=col<n:
            if not visited[row][col] and lst[row][col]==0:
                visited[row][col]=1
                dfs(row,col,tr,tc,position)
                visited[row][col]=0

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
stpt = [list(map(int,input().split())) for _ in range(m)]
visited =[[0 for _ in range(n)] for _ in range(n)]
endrow,endcol = stpt[-1]
cnt = 0
strow,stcol = stpt[0]
nextrow,nextcol = stpt[1]
visited[strow-1][stcol-1] = 1
dfs(strow-1,stcol-1,nextrow-1,nextcol-1,1)
print(cnt)
=======
input = sys.stdin.readline
def dfs(r):
    if r == m:
        print(*lst)
        return
    for i in range(1,n+1):
        lst.append(i)
        dfs(r+1)
        lst.pop()
n,m = map(int,input().split())
visited =[0 for _ in range(n)]
lst = []
dfs(0)
>>>>>>> 875a0b2b2d1657fe9228397c098597f5784f6414
