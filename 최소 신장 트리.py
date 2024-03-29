import heapq

def prim(start):
    pq = []
    dist = 0
    cnt = 0
    heapq.heappush(pq,(0,start))
    while pq:
        nextdist,pt = heapq.heappop(pq)
        if not visited[pt]:
            cnt += 1
            visited[pt] = 1
            dist += nextdist
        else:
            continue
        for i in route[pt]:
            newdist,nextpt = i
            heapq.heappush(pq,(newdist,nextpt))

        if cnt == n+1:
            break
    return dist

for t in range(int(input())):
    n,e = map(int,input().split())
    route = [[] for _ in range(n+1)]
    for _ in range(e):
        s,e,w = map(int,input().split())
        route[s].append((w,e))
        route[e].append((w,s))

    visited = [0] * (n+1)
    result = prim(0)
    print(f'#{t+1} {result}')