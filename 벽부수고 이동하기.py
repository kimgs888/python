import sys
from collections import deque
input = sys.stdin.readline
di,dj  = [1,0,-1,0], [0,1,0,-1]
def bfs(initr,initc):
    q.append((initr,initc,1))
    visited[initr][initc] = 1
    while q:
        r,c,bp = q.popleft()
        for i in range(4):
            row, col = r + di[i], c + dj[i]
            if 0<=row<n and 0<=col<m:
                if bp == 1:
                    if not visited[row][col]:
                        if lst[row][col] == 0:
                            visited[row][col]=visited[r][c] + 1
                            q.append((row,col,bp))
                        else:
                            breakNvisited[row][col] = visited[r][c] + 1
                            q.append((row,col,2))
                elif bp == 2:
                    if not breakNvisited[row][col]:
                        breakNvisited[row][col]= breakNvisited[r][c] + 1
                        if lst[row][col] == 0:
                            q.append((row,col,bp))


n,m = map(int,input().split())
lst = [list(map(int,input().strip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
breakNvisited = [[0 for _ in range(m)] for _ in range(n)]
lst[0][0] = 1
q = deque()
bfs(0,0)
if breakNvisited[n-1][m-1] == 0 and visited[n-1][m-1] == 0:
    result = -1
elif breakNvisited[n-1][m-1] == 0 or visited[n-1][m-1] == 0:
    result = max(breakNvisited[n-1][m-1],visited[n-1][m-1])
else:
    result = min(breakNvisited[n - 1][m - 1], visited[n - 1][m - 1])

print(result)

