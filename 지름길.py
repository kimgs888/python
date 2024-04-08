import sys
import heapq
input = sys.stdin.readline
def dijkstra():
    pq = []
    heapq.heappush(pq,(0,0))
    drive[0] = 0
    while pq:
        move,position = heapq.heappop(pq)
        if position == d:
            return
        if drive[position]<move:
            continue
        if highway[position]:
            for i in highway[position]:
                destination, des_move = i
                next_move = move + des_move
                if drive[destination] > next_move:
                    drive[destination] = next_move
                    heapq.heappush(pq,(next_move,destination))
        if drive[position+1] > move + 1:
            drive[position + 1] = move + 1
            heapq.heappush(pq,(move+1,position+1))
    return


n,d = map(int,input().split())
inf = int(1e9)
highway = [[] for _ in range(d+1)]
drive = [inf] * (d+1)
for i in range(n):
    start,end,distance = map(int,input().split())
    if end>d:
        continue
    highway[start].append((end,distance))

dijkstra()
print(drive[d])
