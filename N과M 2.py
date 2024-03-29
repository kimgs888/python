import sys
input = sys.stdin.readline
def dfs(r):
    if r == m:
        print(*lst)
        return
    for i in range(n):
        if not visited[i]:
            if not len(lst) or lst[-1]<i+1:
                visited[i] = 1
                lst.append(i+1)
                dfs(r+1)
                lst.pop()
                visited[i] = 0

n,m = map(int,input().split())
visited =[0 for _ in range(n)]
lst = []
dfs(0)