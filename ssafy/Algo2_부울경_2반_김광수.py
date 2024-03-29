def dfs(r,build,cost):
    global result
    global resultcost

    if cost>v: # 비용초과
        return

    if build<=result and cost>resultcost:
        return


    if r == n:
        if result < build:  # 최대 다리 건설 조건찾기
            result = build
            resultcost = cost
        elif result == build: # 같은 경우 최소 비용
            resultcost = min(resultcost,cost)
        return


    dfs(r+1,build+1,cost+costlst[r])
    dfs(r+1,build,cost)


for t in range(int(input())):
    n,v = map(int,input().split())
    costlst = list(map(int,input().split()))
    result = 0
    resultcost = int(1e9)
    dfs(0,0,0)

    print(f'#{t+1} {result} {resultcost}')