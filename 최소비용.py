import heapq
di = [1,0,-1,0]
dj = [0,1,0,-1]

def dijstra(initr,initc):
    pq = []
    heapq.heappush(pq,(0,initr,initc))
    fuel[initr][initc] = 0
    while pq:
        leftfuel,row,col = heapq.heappop(pq)
        for i in range(4):
            r = row + di[i]
            c = col + dj[i]
            if 0<=r<n and 0<=c<n:
                if lst[r][c] > lst[row][col]:
                    diffuel = lst[r][c] - lst[row][col]
                else:
                    diffuel = 0

                if fuel[r][c] <= diffuel + 1 + leftfuel:
                    continue
                else:
                    nextfuel = diffuel
                    fuel[r][c] = nextfuel+1 + leftfuel
                    heapq.heappush(pq,(fuel[r][c],r,c))

for t in range(int(input())):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    INF = int(1e9)
    fuel = [[INF for _ in range(n)] for _ in range(n)]

    dijstra(0,0)
    print(f'#{t+1} {fuel[n-1][n-1]}')