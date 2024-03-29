import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0,0))
    while pq:
        dist, pt = heapq.heappop(pq)
        if result[pt] < dist:
            continue
        else:
            result[pt] = dist

        for i in route[pt]:
            nextdist, nextpt = i
            if nextdist>= result[nextpt]:
                continue
            heapq.heappush(pq,(nextdist+dist,nextpt))

for t in range(int(input())):
    n,e = map(int,input().split())
    route = [[] for _ in range(n+1)]
    INF = int(1e9)
    result = [INF for _ in range(n+1)]
    for _ in range(e):
        s,e,w = map(int,input().split())
        route[s].append((w,e))

    dijkstra(0)
    print(f'#{t+1} {result[n]}')