import sys
from collections import deque
n = int(sys.stdin.readline().strip())
lst = list(map(int,sys.stdin.readline().strip().split()))
deck = [i for i in range(1,n+1)]
q = deque()
q.extend(deck)
ans = deque()
i = n-1
while q:
    card = q.popleft()
    if lst[i] == 1:
        ans.appendleft(card)
    elif lst[i] == 3:
        ans.append(card)
    elif lst[i] == 2:
        ans.insert(1,card)
    i -= 1

print(*ans)