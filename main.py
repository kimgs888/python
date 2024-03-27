import sys
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