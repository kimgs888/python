import sys
from collections import deque
input = sys.stdin.readline
q = deque()
n,k = map(int,input().strip().split())

for i in range(1,n+1):
    q.append(i)
i = 0
print('<',end='')
while q:
    if len(q) == 1:
        num = q.popleft()
        print(num,end='>')
        break
    num = q.popleft()
    if i == k-1:
        print(num,end=', ')
        i = 0
        continue
    q.append(num)
    i += 1
print()