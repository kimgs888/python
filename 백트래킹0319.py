# 중복된 수열
# 1~3 까지 숫자 배열이 있을 때
# 111,112,~,332,333

def numlst(c):
    if c == n:
        print(result)
        copyresult = result.copy()
        ans.append(copyresult)
        return

    for i in range(n):
        if arr[i] in result:
            continue
        result[c]= arr[i]
        numlst(c + 1)
        result[c] = 0

arr = [i for i in range(1,4)]
n = len(arr)
result = [0]*n
visited = [0]*(n+1)
ans = []
numlst(0)
print(ans)