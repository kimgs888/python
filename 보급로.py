import heapq
di = [1,0,-1,0]
dj = [0,1,0,-1]

def dijkstra(initr,initc):
    pq = []
    heapq.heappush(pq,(0,initr,initc))
    worktime[initr][initc] = 0

    while pq:
        t,r,c = heapq.heappop(pq)
        visited[r][c] = 1

        for i in range(4):
            row = r + di[i]
            col = c + dj[i]
            if 0<=row<n and 0<=col<n:
                time = lst[row][col]+t
                if time < worktime[row][col]:
                    worktime[row][col] = time
                    heapq.heappush(pq,(time,row,col))



for t in range(int(input())):
    n = int(input())
    INF = int(1e9)
    lst = [list(map(int,input())) for _ in range(n)]
    worktime = [[INF for _ in range(n)] for _ in range(n)]
    visited =  [[0 for _ in range(n)] for _ in range(n)]
    dijkstra(0,0)
    print(f'#{t+1} {worktime[n-1][n-1]}')