import heapq

def dijstra(start):
    pq = []
    timeto[start] = 0
    heapq.heappush(pq,(start,0))
    while pq:
        v,time = heapq.heappop(pq)
        for i in route[v]:
            direction, nexttime = i
            if timeto[direction] > nexttime + time:
                newtime = nexttime + time
                timeto[direction] = newtime
                heapq.heappush(pq,(direction,newtime))

def prim(start):
    pq = []
    visited = [0] * (n + 1)
    heapq.heappush(pq,(0,start))

    while pq:
        dist,currentpt = heapq.heappop(pq)

        if visited[currentpt]:
            continue

        visited[currentpt] = 1


        if currentpt == pt:
            return dist

        for i in route[currentpt]:
            nextpt,nextdist = i
            heapq.heappush(pq,(nextdist+dist,nextpt))

for t in range(int(input())):
    n,m,pt = map(int,input().split())
    route = [[] for _ in range(n+1)]
    INF = int(1e9)
    timeto = [INF] * (n+1)
    for _ in range(m):
        x,y,c = map(int,input().split())
        route[x].append((y,c))

    dijstra(pt)
    dict = {}
    for i in range(1,n+1):
        if i == pt:
            continue
        else:
            returntime = prim(i)
            timeto[i] += returntime
    timeto[0] = 0
    print(f'#{t+1} {max(timeto)}')
