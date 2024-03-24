import sys
input = sys.stdin.readline
n = int(input().strip())
lst = list(map(int,input().strip().split()))
stack = []
result = []
for i in range(n):
    while 1:
        if len(stack)==0:
            result.append(0)
            stack.append([lst[i],i+1])
            break
        else:
            topheight,idx = stack.pop()
            if lst[i]<topheight:
                result.append(idx)
                stack.append([topheight,idx])
                stack.append([lst[i], i + 1])
                break
print(*result)