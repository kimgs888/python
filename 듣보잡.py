import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())

nolooklst = [input().strip() for _ in range(n+m)]
nolooklst.sort()
cklen = set(nolooklst)
print(n+m-len(cklen))
for i in range(n+m-1):
    if nolooklst[i] == nolooklst[i+1]:
        print(nolooklst[i])