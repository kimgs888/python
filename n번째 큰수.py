import sys
import heapq
input = sys.stdin.readline
n = int(input().strip())
hq = []
for _ in range(n):
    for i in list(map(int,input().strip().split())):
        heapq.heappush(hq, i)
        if len(hq)>n:
            heapq.heappop(hq)

print(heapq.heappop(hq))


