# 0129 prb1 전기버스
# n = int(input())
# for case in range(n):
#     # print('case=',case)
#     busMove,totalDistance,totalStaion = map(int,input().split())
#     stationLocs = list(map(int,input().split()))
#     # print(busMove,totalDistance,totalStaion,stationLocs)
#     result =0
#     for stationIndex in range(len(stationLocs)-1):
#         if (stationLocs[stationIndex+1]-stationLocs[stationIndex]) > busMove:
#             result = result -1
#             break
#     if result == -1:
#         print(f'#{case+1} 0')
#         continue
#     startPosition = 0
#     cnt = 0
#     stationLocs.append(totalDistance)
#     while 1:
#         for stationIndex in range(len(stationLocs)-1,-1,-1):
#             if (stationLocs[stationIndex]-startPosition<=busMove):
#                 startPosition = stationLocs[stationIndex]
#                 cnt = cnt + 1
#                 break
#         # print(startPosition)
#         if startPosition == stationLocs[totalStaion]:
#             cnt = cnt -1
#             break
#     print(f'#{case+1} {cnt}')

# prb 4 min max
# cases = int(input())
# for case in range(cases):
#     numbers = int(input())
#     arr = list(map(int,input().split()))
#     print(f'#{case+1} {max(arr)-min(arr)}')

# prb 구간합
# cases = int(input())
# for case in range(cases):
#     totalNum, countNum = map(int,input().split())
#     numList = list(map(int,input().split()))
#     sumList = []
#     for numIdx in range(totalNum-countNum+1):
#         sumNum = 0
#         for sumIdx in range(countNum):
#             sumNum = sumNum + numList[sumIdx+numIdx]
#         sumList.append(sumNum)
#     print(f'#{case+1} {max(sumList)-min(sumList)}')

# prb 숫자카드
# cases = int(input())
# for case in range(cases):
#     cardNum = int(input())
#     cardList = list(map(str,input()))
#     countCard = 0
#     findCard = 10
#     while cardList:
#         cardList.sort()
#         card = cardList.pop()
#         tempCount = cardList.count(card)+1
#         if countCard<tempCount:
#             countCard = tempCount
#             findCard = card
#     print(f'#{case+1} {findCard} {countCard}')

#prb 사전학습 숫자배열 회전
# cases = int(input())
# for case in range(cases):
#     print('case=',case)
#     arrSize = int(input())
#     arrList = []
#     for _ in range(arrSize):
#         arr = list(map(int,input().split()))
#         arrList.append(arr)
#     for idx in range(arrSize):
#         for idy in range(arrSize):
#             print(idx,idy)
#         # arrList[0][0],arrList[0][idx],arrList[idx][idx],arrList[idx][0] = arrList[idx][0],arrList[0][0],arrList[0][idx],arrList[idx][idx]
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     mat = list(list(map(str, input().split())) for _ in range(N))
#     ans = ["s"] * N
#
#     # for j in range(N):
#     #     for i in range(N - 1, -1, -1):
#     #         ans[j] += mat[i][j]
#     #     ans[j] += " "
#
#     # for j in range(1, N + 1):
#     #     for i in range(N - 1, -1, -1):
#     #         ans[j - 1] += mat[-j][i]
#     #     ans[j - 1] += " "
#     #
#     # for j in range(1, N + 1):
#     #     for i in range(N):
#     #         ans[j - 1] += mat[i][-j]
#
#     final_ans = "\n".join(ans)
#     print(f'#{test_case}\n{final_ans}')
# def selfNum(nums):
#     # print(len(str(nums)))
#     addNum = nums
#     for num in list(str(nums)):
#         addNum = addNum+int(num)
#     return addNum
#
# numList = [i for i in range(1,10000)]
# result = 0
# count = 1
# while count <=10000:
#     result = selfNum(count)
#     if result in numList:
#         numList.remove(result)
#     count = count + 1
# for i in numList:
#     print(i)

# case = int(input())
# for t in range(case):
#     n = int(input())
#     print(f'#{t+1}')
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     arr = [[0]*n for _ in range(n)]
#     num = 1
#     direction = 0
#     pos = [0,0]
#     while num <=n*n:
#         arr[pos[0]][pos[1]]=num
#         if direction == 0:
#             if pos[1]+1>=n or arr[pos[0]][pos[1]+1] != 0:
#                 direction = 1
#             else:
#                 pos[0] =pos[0]+di[0]
#                 pos[1] =pos[1]+dj[0]
#         if direction == 1:
#             if pos[0]+1>=n or arr[pos[0]+1][pos[1]] != 0:
#                 direction = 2
#             else:
#                 pos[1] = pos[1] + dj[1]
#                 pos[0] = pos[0] + di[1]
#         if direction == 2:
#             if pos[1]<=0 or arr[pos[0]][pos[1]-1] != 0:
#                 direction = 3
#             else:
#                 pos[0] = pos[0] + di[2]
#                 pos[1] = pos[1] + dj[2]
#         if direction == 3:
#             if pos[0]<=0 or arr[pos[0]-1][pos[1]] != 0:
#                 direction = 0
#                 pos[0] = pos[0] + di[0]
#                 pos[1] = pos[1] + dj[0]
#             else:
#                 pos[0] = pos[0] + di[3]
#                 pos[1] = pos[1] + dj[3]
#         num = num+1
#     for i in range(n):
#         for j in range(n):
#             print(arr[i][j],end=' ')
#         print()

# N = int(input())
# if N <=99:
#     cnt = N
# else:
#     cnt = 99
#     for i in range(100,N+1):
#         findList = list(map(int, list(str(i))))
#         difNum = findList[0] - findList[1]
#         findNum = findList[1] - findList[2]
#         if difNum == findNum:
#             cnt = cnt + 1
# print(cnt)
# 숫자를 정렬하자
# for t in range(int(input())):
#     print(f"#{t+1} ",end='')
#     numLen = int(input())
#     numList = list(map(int,input().split()))
#
#     for i in range(numLen-1):
#         idx = i
#         for j in range(idx+1,numLen):
#             if numList[j]<numList[idx]:
#                 idx = j
#         numList[i], numList[idx] = numList[idx],numList[i]
#     print(*numList)
# 특별한 정렬
# for t in range(int(input())):
#     print(f"#{t+1} ",end='')
#     numLen = int(input())
#     numList = list(map(int,input().split()))
#     for i in range(numLen):
#         idx = i
#         if idx%2 ==1:
#             for j in range(idx+1,numLen):
#                 if numList[j]<numList[idx]:
#                     idx = j
#             numList[i], numList[idx] = numList[idx],numList[i]
#         else:
#             for j in range(idx+1,numLen):
#                 if numList[j]>numList[idx]:
#                     idx = j
#             numList[i], numList[idx] = numList[idx],numList[i]
#     print(*numList[:10])
# 이진 탐색
# for t in range(int(input())):
#     aLen,bLen = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     a.sort()
#     b.sort()
#     cnt = 0
#     for bIdx in range(bLen):
#         l = 0
#         r = aLen-1
#         turn =0
#         while l<=r:
#             mid = (r+l)//2
#             if b[bIdx]==a[mid]:
#                 cnt = cnt + 1
#                 break
#             elif b[bIdx]>a[mid]:
#                 if turn == 'left':
#                     break
#                 l = mid + 1
#                 turn = 'left'
#             else:
#                 if turn == 'right':
#                     break
#                 r = mid - 1
#                 turn = 'right'
#     print(f"#{t+1} {cnt}")
# 영화감독 숌
# N = int(input())
# num =666
# cnt = 0
# while 1:
#     tmpNum = str(num)
#     if '666' in tmpNum:
#         cnt = cnt + 1
#     if N == cnt:
#         print(num)
#         break
#     num = num + 1

# 풍선팡
#
# for t in range(int(input())):
#     r, c = list(map(int,input().split()))
#     ball = [list(map(int,input().split())) for _ in range(r)]
#     di = [1,0,-1,0]
#     dj = [0,-1,0,1]
#     sumList=[]
#     result = 0
#     for i in range(r):
#         for j in range(c):
#             addNum = ball[i][j]
#             for k in range(4):
#                 for l in range(1,ball[i][j]+1):
#                     if 0<=(i+(di[k]*l))<r and 0<=(j+(dj[k]*l))<c:
#                         addNum = addNum + ball[i+(di[k]*l)][j+(dj[k]*l)]
#             sumList.append(addNum)
#             if result<addNum:
#                 result=addNum
#     print(result)
#     print(f'#{t+1} {max(sumList)}')

#베이비진
# for t in range(int(input())):
#     numList = input().split()
#     number = numList[0]
#     counter_ = [0]*10
#     for i in range(len(number)):
#         counter_[int(number[i])] = counter_[int(number[i])] + 1
#     c = 0
#     triplet = 0
#     run_ = 0
#     while 1:
#         if counter_[c] >= 3:
#             counter_[c] = counter_[c] - 3
#             triplet = triplet + 1
#             continue
#         # for i in range(3):
#         #     if c+i<=9 and counter[c+i]>=1:
#         #         counter[c+i] = counter[c+i]-1
#         #         run = run + 1
#         #         continue
#
#         if c+2<=9 and counter_[c]>=1 and counter_[c+1]>=1 and counter_[c+2]>=1:
#             counter_[c] = counter_[c] - 1
#             counter_[c+1] = counter_[c+1] - 1
#             counter_[c+2] = counter_[c+2] - 1
#             run_ = run_ + 1
#             continue
#         if c == 9:
#             break
#         c = c + 1
#     result = 'false'
#     if triplet+run_ == 2:
#         result = 'true'
#     print(f'#{t+1} {result}')

# 퇴사
# n = int(input())
# dp = [0]*(n+1)
# lst = [list(map(int,input().split())) for _ in range(n)]
#
# for i in range(n):
#     t = lst[i][0]
#     p = lst[i][1]
#
#     if i+t>n:
#         continue
#     else:
#         dp[i] = max(dp[:i+1])
#         dp[i+t] = max(dp[i]+p,dp[i+t])
# result = max(dp)
# print(result)
# #----------------------------------
# def brute_force(day, total_profit, N, schedule):
#     global max_profit
#
#     if day == N:
#         max_profit = max(max_profit, total_profit)
#         return
#
#     # 상담을 하는 경우
#     next_day, profit = schedule[day]
#     if day + next_day <= N:
#         brute_force(day + next_day, total_profit + profit, N, schedule)
#
#     # 상담을 하지 않는 경우
#     brute_force(day + 1, total_profit, N, schedule)
#
# # 입력 받기
# N = int(input())
# schedule = [tuple(map(int, input().split())) for _ in range(N)]
#
# max_profit = 0
# brute_force(0, 0, N, schedule)
#
# print(max_profit)

# 두수의 합
# n,m = map(int,input().split())
# lst = list(map(int,input().split()))
# newlst = lst
# cnt = 0
# for i in range(n):
#     cnt = cnt + lst.count(m)
#     newlst=newlst[1:]
#     lst = [x + y for x, y in zip(lst, newlst)]
# print(cnt)
# for i in range(n):
#     ans = 0
#     j = 0
#
#     while i+j<n:
#         ans = ans + lst[i+j]
#         if ans<m:
#             j=j+1
#         elif ans == m:
#             cnt = cnt + 1
#             break
#         else:
#             break

# print(cnt)
# a=[1,2,3]
# b=[3,4,5,1]
# print(b[1:])
# c=[x+y for x,y in zip(a, b)]
# print(c)

#모든수열
# n = 3
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if b != a:
#             for c in range(1,n+1):
#                 if c != a and c !=b:
#                     print(a,b,c)
# from itertools import permutations
# n = int(input())
# data = [i for i in range(1,n+1)]
# c=list(permutations(data,n))
# for num in c:
#     print(*num)

# 일곱난쟁이
# def height(lst,goal):
#     for i in lst:
#         for j in lst:
#             if i != j and i+j == goal:
#                 lst.remove(i)
#                 lst.remove(j)
#                 return lst
#
# lst = [int(input()) for _ in range(9)]
# newlst = height(lst,sum(lst)-100)
# newlst.sort()
# a = [print(i) for i in newlst]

# 문서 검색
# string = input()
# char = input()
# sl = len(string)
# cl = len(char)
# i = 0
# cnt = 0
# while i <= sl-cl:
#     if string[i:i+cl]==char:
#         i = i + cl
#         cnt = cnt + 1
#         continue
#     i = i + 1
# print(cnt)

# # [S/W 문제해결 기본] 4일차 - 길찾기
# for t in range(10):
#     tc, n = map(int,input().split())
#     lst = list(map(int,input().split()))
#     dir = [[] for _ in range(n+1)]
#     for i in range(n):
#         dir[lst[i*2]].append(lst[i*2+1])
#
#     result = 0
#     stack = []
#     memory = [0]*100
#     v = 0
#     stack.append(v)
#     while 1:
#         if v == 99:
#             result =1
#             break
#         memory[v] = 1
#         for i in dir[v]:
#             if not memory[i]:
#                 v=i
#                 stack.append(i)
#                 break
#         else:
#             if not stack:
#                 break
#             else:
#                 v = stack.pop()
#
#     print(f'#{tc} {result}')

# 그래프 경로
# for t in range(int(input())):
#
#     v,e = map(int,input().split())
#     route = [list(map(int,input().split())) for _ in range(e)]
#     s,g = map(int,input().split())
#
#     check = [0]*(v+1)
#     stack = []
#     result = 0
#     lst =[[] for _ in range(v+1)]
#
#     for i in range(len(route)):
#         lst[route[i][0]].append(route[i][1])
#
#     v = s
#     stack.append(v)
#
#     while 1:
#
#         if v == g:
#             result = 1
#             break
#
#         for i in lst[v]:
#
#             if check[i]:
#                 continue
#             else:
#                 v = i
#                 stack.append(i)
#                 check[i] = 1
#                 break
#         else:
#
#             if stack:
#                 v = stack.pop()
#             else:
#                 break
#
#     print(f'#{t+1} {result}')

# n = int(input())
# lst = list(map(int,input().split()))
#
# lst.sort(reverse=1)
# result = 0
#
# if n%2 ==0:
#
#     half = int(n/2)-1
#     result = result + lst[half]
#     result = result - lst[(half)+1]
#
#     for i in range((half)):
#         result = result + (lst[i]*2)
#         result = result - (lst[(n-1)-i]*2)
#
# else:
#
#     half = int(n // 2)
#
#     for i in range((half)):
#         result = result + (lst[i]*2)
#         result = result - (lst[(n-1)-i]*2)
#
#     if abs(lst[half]-lst[half+1]) > abs(lst[half]-lst[half-1]):
#         result = result - (lst[half-1])
#         result = result + (lst[half])
#     else:
#         result = result + (lst[half+1])
#         result = result - (lst[half])
#
# print(result)

# 팩토리얼
# # 반복적으로 구현한 n!
# def factorial_iterative(n):
#     result = 1
#
#     for i in range(1,N+1):
#         result *= i
#     return result
#
# # 재귀적으로 구현
# def factorial_recursive(n):
#     if n <= 1: # n이 1 이하인 경우 1 반환
#         return 1
#     return n* factorial_recursive(n-1)

# 연산자 끼워넣기
# def compute(comp):
#     result = lst[0]
#
#     for i in range(N-1):
#         if comp[i] == 0:
#             result = result + lst[i+1]
#         elif comp[i] == 1:
#             result = result - lst[i+1]
#         elif comp[i] == 2:
#             result = result * lst[i+1]
#         elif comp[i] == 3:
#
#             if result < 0:
#                 result = -(abs(result)//lst[i+1])
#             else:
#                 result = result//lst[i+1]
#
#     return result
#
# from itertools import permutations
#
# N = int(input())
# lst = list(map(int,input().split()))
# compTemp = list(map(int,input().split()))
#
# comp = [i for i in range(len(compTemp)) for j in range(compTemp[i])]
# ans = []
# compComb = set(permutations(comp,N-1))
# for cal in compComb:
#     ans.append(compute(cal))
#
#
# print(max(ans))
# print(min(ans))


# def calc(i, current):
#     global max_num, min_num, N, num, operator
#     if N == i:
#         max_num = max(max_num, current)
#         min_num = min(min_num, current)
#     else:
#         if operator[0]:
#             operator[0] -= 1
#             calc(i + 1, current + num[i])
#             operator[0] += 1
#         if operator[1]:
#             operator[1] -= 1
#             calc(i + 1, current - num[i])
#             operator[1] += 1
#         if operator[2]:
#             operator[2] -= 1
#             calc(i + 1, current * num[i])
#             operator[2] += 1
#         if operator[3]:
#             operator[3] -= 1
#             if current < 0:
#                 tmp = -(-current // num[i])
#             else:
#                 tmp = current // num[i]
#             calc(i + 1, tmp)
#             operator[3] += 1
#
# N = int(input())
# num = list(map(int, input().split()))
# operator = list(map(int, input().split()))
# max_num = -100000000
# min_num = 100000000
#
# calc(1, num[0])
#
# print(max_num)
# print(min_num)

# 바이러스
# def dfs(i,net,check):
#     check[i] = True
#     # print(i)
#
#     for j in net[i]:
#         if not check[j]:
#             dfs(j,net,check)
#
#
# num = int(input())
# n = int(input())
# lst = [list(map(int,input().split())) for _ in range(n)]
#
# net = [[] for _ in range(num+1)]
# for i in lst:
#     net[i[0]].append(i[1])
#     net[i[1]].append(i[0])
#
# check = [False]*(num+1)
#
# v = 1
#
# dfs(v,net,check)
#
# print(sum(check)-1)

# 유기농 배추
# import sys
# sys.setrecursionlimit(10**7)
# def dfs(r,c):
#     if r < 0 or r >= n or c < 0 or c >= m:
#         return False
#
#     if lst[r][c]:
#         lst[r][c] = 0
#         dfs(r+1,c)
#         dfs(r-1,c)
#         dfs(r,c+1)
#         dfs(r,c-1)
#         return True
#
#     return False
#
# for t in range(int(input())):
#     m,n,k = map(int,input().split()) # 열 m,c / 행 n,r
#     lst = [[0]*m for _ in range(n)]
#
#     for i in range(k):
#         c,r = map(int,input().split())
#         lst[r][c] = 1
#
#     cnt = 0
#
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j):
#                 cnt = cnt + 1
#
#     print(cnt)

# DFS와 BFS
# def dfs(v):
#     check[v] = 1
#     print(v,end=' ')
#     route[v].sort()
#     for i in route[v]:
#         if not check[i]:
#             dfs(i)
#
# def bfs(v):
#     queue = deque([v])
#     checkbfs[v] = 1
#     while queue:
#         w = queue.popleft()
#         print(w,end= ' ')
#         for i in route[w]:
#             if not checkbfs[i]:
#                 queue.append(i)
#                 checkbfs[i] = 1
#
# from collections import deque
# n,m,v = map(int,input().split())
# lst = [list(map(int,input().split())) for _ in range(m)]
#
# check = [0]*(n+1)
# checkbfs = [0]*(n+1)
# route = [[] for _ in range(n+1)]
#
# for i in lst:
#     route[i[0]].append(i[1])
#     route[i[1]].append(i[0])
#
# dfs(v)
# print()
# bfs(v)

# 연결 요소의 개수
# def dfs(v):
#     check[v] = 1
#     for i in route[v]:
#         if not check[i]:
#             dfs(i)
#
# import sys
# sys.setrecursionlimit(10**7)
# m,n = map(int,sys.stdin.readline().split())
# check = [0] * (m+1)
# route = [[] for _ in range(m+1)]
# lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#
# for i in lst:
#     route[i[0]].append(i[1])
#     route[i[1]].append(i[0])
#
# cnt = 0
# for i in range(1,m+1):
#     if not check[i]:
#         dfs(i)
#         cnt = cnt + 1
#
#
# print(cnt)

# 섬의 개수
# import sys
# sys.setrecursionlimit(10**7)
#
# def dfs(r,c):
#     if r < 0 or r >= h or c < 0 or c >= w:
#         return False
#
#     if lst[r][c]:
#         lst[r][c] = 0
#         dfs(r+1,c)
#         dfs(r+1,c+1)
#         dfs(r,c+1)
#         dfs(r-1,c+1)
#         dfs(r-1,c)
#         dfs(r-1,c-1)
#         dfs(r,c-1)
#         dfs(r+1,c-1)
#         return True
#
#     return False
#
#
# while 1:
#     w,h = map(int,sys.stdin.readline().split())
#
#     if not w:
#         break
#
#     lst = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if lst[i][j]:
#                 dfs(i,j)
#                 cnt = cnt + 1
#
#     print(cnt)

# 수건돌리기
# import sys
# def findPat(n,k,c):
#     if n % 2==0:
#         if n//2 >= k:
#             ans = (2*k-1) * (2**c)
#             return ans
#     else:
#         if n//2 + 1 >= k:
#             return (2*k-1) * (2**c)
#
#
# n,k = map(int,sys.stdin.readline().split())
# print(findPat(n,k,0))

# 후위 표기식
# import sys
# lst = (sys.stdin.readline())
# comp = list('('+lst+')')
# isp = {'(': 0,'*': 2,'/': 2,'+':1,'-':1,')':-1}
# icp = {'(': 3,'*': 2,'/': 2,'+':1,'-':1,')':-1}
#
# ans = ''
# stack = []
#
# for i in comp:
#     if i.isalpha():
#         ans = ans + i
#     else:
#         if i == '(':
#             stack.append(i)
#         elif i == ')':
#             while 1:
#                 cal = stack.pop()
#                 if cal =='(':
#                     break
#                 ans = ans + cal
#         elif i in '*/-+' and isp[stack[-1]]<icp[i]:
#             stack.append(i)
#         elif i in '*/-+' and isp[stack[-1]] >= icp[i]:
#             while 1:
#                 if isp[stack[-1]] < icp[i]:
#                     break
#                 cal = stack.pop()
#                 ans = ans + cal
#             stack.append(i)
#
# print(ans)

# 다솔이의 다이아몬드 장식
# for t in range(int(input())):
#     string = input()
#     n = len(string)
#     col = 1+(n*4)
#     lst = [['.']*col for _ in range(5)]
#     ans = [2+(4*i) for i in range(n)]
#     for i in range(5):
#         for j in range(col):
#             if i ==1 or i == 3:
#                 if j%2==1:
#                     lst[i][j] = '#'
#             if i ==0 or i==4:
#                 if j in ans:
#                     lst[i][j] = '#'
#             if i == 2:
#                 if j%2==0:
#                     lst[i][j] = '#'
#                 if j in ans:
#                     lst[i][j] = string[0]
#                     string = string[1:]
#         print(''.join(lst[i]))

# 간단한 압축 풀기
# for t in range(int(input())):
#     print(f'#{t+1}')
#     n = int(input())
#     string = ''
#     for i in range(n):
#         char,cnt = map(str,input().split())
#         string = string + (char * int(cnt))
#
#     while string:
#         print(string[:10])
#         string = string[10:]

# 다음 소수 찾기
# import sys
# for t in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     ans = n
#     if ans < 2:
#         print(2)
#         continue
#     findN = 1
#     while 1:
#         for i in range(2,int(ans**0.5)+1):
#             if ans%i == 0:
#                 break
#         else:
#             findN = 0
#
#         if not findN:
#             break
#
#         ans = ans + 1
#
#     print(ans)

# import sys
# n = int(input())
# for i in range(1,n+1):
#     print((n-i)*' ',end='')
#     print('*'*i)

# 자기 방으로 돌아가기

# for t in range(int(input())):
#     n = int(input())
#     lst = [list(map(int,input().split())) for _ in range(n)]
#     ans = [0]*400
#     for i in lst:
#         a,b = i
#         if not a%2:
#             a = a - 1
#         if not b%2:
#             b = b - 1
#         if a > b:
#             a,b = b,a
#         for j in range(a,b+1):
#             ans[j] = ans[j] + 1
#
#     print(f'#{t+1} {max(ans)}')
# import sys
# n = int(sys.stdin.readline())
# lst = [int(sys.stdin.readline()) for _ in range(n)]
# visited = [0]*(n+1)
# result = []
# ans = 1
# if n == 1:
#     result.append('+')
#     result.append('-')
# else:
#     for i in range(n-1):
#         if i == 0:
#             visited[lst[i]] = 1
#             for _ in range(lst[i]):
#                 result.append('+')
#             result.append('-')
#
#         if lst[i]<lst[i+1]:
#             tmp = lst[i+1]
#             visited[tmp] = 1
#             result.append('+')
#             while 1:
#                 tmp = tmp - 1
#                 if visited[tmp] == 1:
#                     break
#                 result.append('+')
#             result.append('-')
#
#         elif lst[i]>lst[i+1]:
#             dif = lst[i]-lst[i+1]
#             if dif == 1:
#                 result.append('-')
#                 visited[lst[i+1]] = 1
#             else:
#                 for j in range(lst[i]-1,lst[i+1],-1):
#                     if visited[j] == 1:
#                         pass
#                     else:
#                         ans = 0
#                 result.append('-')
#                 visited[lst[i+1]] = 1
#
# if ans:
#     for i in result:
#         print(i)
# else:
#     print('NO')

# 단지번호붙이기
# import sys
# from collections import deque
#
# di = [1,0,-1,0]
# dj = [0,1,0,-1]
#
# def bfs(row,col,lst):
#     global num
#     q = deque()
#     q.append([row,col])
#     num = num + 1
#     lst[row][col] = num
#
#     while q:
#         r,c = q.popleft()
#         for i in range(4):
#             tmpr = r+di[i]
#             tmpc = c+dj[i]
#             if 0<=tmpr<n and 0<=tmpc<n and lst[tmpr][tmpc] == 1:
#                 q.append([tmpr,tmpc])
#                 lst[tmpr][tmpc] = num
#
#     return
#
# n = int(sys.stdin.readline())
# lst = [list(map(int,input())) for _ in range(n)]
# num = 1
# for i in range(n):
#     for j in range(n):
#         if lst[i][j] == 1:
#             bfs(i,j,lst)
# print(num-1)
# ans = []
#
# for j in range(n):
#     ans.extend(lst[j])
#
# result = [ans.count(k) for k in range(2,num+1)]
# result.sort()
#
# if not result:
#     print(0)
#
# a = [print(result[l]) for l in range(num-1)]

# 스택
# def push1(num):
#     ans.append(num)
#
# def pop1():
#     if ans:
#         print(ans.pop())
#     else:
#         print(-1)
#
# def size1():
#     print(len(ans))
#
# def empty1():
#     if len(ans):
#         print(0)
#     else:
#         print(1)
#
# def top1():
#     if ans:
#         print(ans[-1])
#     else:
#         print(-1)
#
#
# n = int(input())
# lst = [list(map(str,input().split())) for _ in range(n)]
# ans =[]
#
# for i in lst:
#     if i[0]=='push':
#         push1(int(i[1]))
#     elif i[0]=='pop':
#         pop1()
#     elif i[0]=='empty':
#         empty1()
#     elif i[0]=='top':
#         top1()
#     elif i[0]=='size':
#         size1()

# 차르봄바
# di = [1,0,-1,0]
# dj = [0,1,0,-1]
#
# def killvir(r,c):
#
#     sumvir = virus[r][c]
#
#     for i in range(1,p+1):
#         for j in range(4):
#             tmpr = r+di[j]*i
#             tmpc = c+dj[j]*i
#             if 0<=tmpr<n and 0<=tmpc<n:
#                 sumvir = sumvir + virus[tmpr][tmpc]
#
#     virtarget.append(sumvir)
#
# for t in range(int(input())):
#
#     n,p = map(int,input().split())
#     virus = [list(map(int,input().split())) for _ in range(n)]
#
#     virtarget = []
#
#     for i in range(n):
#         for j in range(n):
#             killvir(i,j)
#
#     print(f'#{t+1} {max(virtarget)}')

# 사각형 그리기 게임

# for t in range(int(input())):
#     n  = int(input())
#     box = [list(map(int,input().split())) for _ in range(n)]
#
#     numbox = [[] for _ in range(21)]
#     ans = []
#
#     for i in range(n):
#         for j in range(n):
#             numbox[box[i][j]].append([i,j])
#
#     for n in numbox:
#         if n:
#             for fpt in n:
#                 for spt in n:
#                     if fpt[0] <= spt[0] and fpt[1] <= spt[1]:
#                         ans.append((spt[0]-fpt[0]+1)*(spt[1]-fpt[1]+1))
#
#     print(f'#{t+1} {ans.count(max(ans))}')

# solved.ac
# import sys
# n = int(sys.stdin.readline().strip())
# EPS = 1e-9
#
# lst = [int(sys.stdin.readline().strip()) for _ in range(n)]
# if n ==0:
#     print(0)
# elif n:
#     limit = round(n*0.15+EPS)
#     lst.sort()
#     ans = 0
#     div = 0
#     for i in range(limit,n-limit):
#         ans = ans + lst[i]
#         div = div + 1
#
#     print(round((ans/div)+EPS))

# import sys
# n = int(sys.stdin.readline().strip())
# lst = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
# lst.sort()
# for i in lst:
#     print(*i)

# 답안지 채점
# for t in range(int(input())):
#     n,m = map(int,input().split())
#     anslst = list(map(int, input().split()))
#
#     scorelst = []
#
#     for i in range(n):
#         slst = list(map(int,input().split()))
#         tscore = 0
#         score = 0
#         for j in range(m):
#             if anslst[j] == slst[j]:
#                 score = score + 1
#                 tscore = tscore + score
#             else:
#                 score = 0
#         scorelst.append(tscore)
#
#     print(f'#{t+1} {(max(scorelst)-min(scorelst))}')

# 중계기
# print(1+(3.9999)//1)
# for t in range(int(input())):
#     n = int(input())
#     lst = [list(map(int,input().split())) for _ in range(n+1)]
#     hidx = []
#     for i in range(n+1):
#         for j in range(n+1):
#             if lst[i][j] == 2:
#                 fidx  = [i,j]
#             if lst[i][j] == 1:
#                 hidx.append([i,j])
#
#     ans = []
#     xi,yi = fidx
#     for i in hidx:
#         x,y = i
#         if (((x-xi)**2 + (y-yi)**2)**(1/2))//1 == (((x-xi)**2 + (y-yi)**2)**(1/2)):
#             r = (((x-xi)**2 + (y-yi)**2)**(1/2))//1
#         else:
#             r = 1 + (((x-xi)**2 + (y-yi)**2)**(1/2))//1
#         ans.append(r)
#
#     print(f'#{t+1} {int(max(ans))}')

# 이진 힙

# def addnum(v):
#     ans[v] = lst[v]
#
#     while v > 1 and ans[v//2] > ans[v]:
#         ans[v//2],ans[v] = ans[v],ans[v//2]
#         v = v//2
#
#
# for t in range(int(input())):
#     n = int(input())
#     lst = list(map(int,input().split()))
#     lst = [0] + lst
#
#     ans = [0]*(n+1)
#     [addnum(i) for i in range(1,n+1)]
#
#     result = 0
#     tmp = n//2
#
#     while 1:
#         result = result + ans[tmp]
#         tmp = tmp//2
#         if not tmp:
#             break
#
#     print(f'#{t+1} {result}')

# 재미있는 오셀로 게임
# di = [1,0,-1,0,1,-1,-1,1]
# dj = [0,1,0,-1,1,1,-1,-1]
# for t in range(int(input())):
#     n,m = map(int,input().split())
#     MAP = [[-1]*(n+2) for _ in range(n+2)]
#
#     MAP[n//2][n//2] = 2
#     MAP[n//2+1][n//2] = 1
#     MAP[n//2][n//2+1] = 1
#     MAP[n//2+1][n//2+1] = 2
#
#
#     for i in range(m):
#         x,y,c = map(int,input().split())
#         MAP[x][y] = c
#         for j in range(8):
#             tmpx = x+di[j]
#             tmpy = y+dj[j]
#             if MAP[tmpx][tmpy] == 3-c: # 8방향으로 다음 돌이 다른 색이 있다
#                 for k in range(1,n+1):
#                     fndx = x+(di[j]*k)
#                     fndy = y+(dj[j]*k)
#                     if MAP[fndx][fndy] == -1:
#                         break
#                     if MAP[fndx][fndy] == c: # 8방향으로 같은 색의 돌이 나온다
#                         for l in range(k,0,-1):
#                             MAP[x + (di[j] * l)][y + (dj[j] * l)] = c
#                         break
#
#     ans = []
#     for i in range(n+2):
#         ans.extend(MAP[i])
#
#     print(f'#{t+1} {ans.count(1)} {ans.count(2)}')
# 크게 만들기
# import sys
# n,k = map(int,sys.stdin.readline().strip().split())
# lst = list(map(int,sys.stdin.readline().strip()))
# result = []
# result.append(0)
# pt = 0
# k = k + 1   # 0 추가한거 cnt 1 추가while k:
#
#     if k == n-pt:
#         lst = []
#         break
#
#     for i in range(k):
#         if lst[i+pt] > result[-1]:
#             idx = i
#             result.pop()
#             result.append(lst[i + pt])
#             pt = pt + idx + 1
#             k = k - idx - 1
#             break
#     else:
#         result.append(lst[pt])
#         pt = pt + 1
#
# print(''.join(list(map(str,result))),end='')
# for i in range(pt,n):
#     print(lst[i],end='')
# print()
# # result.extend(lst[pt:])
# # print(''.join(list(map(str,result))))

# import sys
# n,k = map(int,sys.stdin.readline().strip().split())
# lst = list(map(int,sys.stdin.readline().strip()))
# stack = []
# cnt = k
# for i in range(n):
#     while(cnt>0 and stack and stack[-1] < lst[i]):
#         stack.pop()
#         cnt = cnt - 1
#     stack.append(lst[i])
# print(''.join(list(map(str,stack[:n-k]))))

# 주식
# import sys
# for t in range(int(sys.stdin.readline().strip())):
#     n = int(sys.stdin.readline().strip())
#     lst = list(map(int,sys.stdin.readline().strip().split()))
#     maxN = lst[n-1]
#     ans = 0
#     for i in range(n-2,-1,-1):
#         if maxN>lst[i]:
#             ans = ans + (maxN-lst[i])
#         else:
#             maxN = lst[i]
#     print(ans)

# 보물

# import sys
# n = int(sys.stdin.readline().strip())
# lsta = list(map(int,sys.stdin.readline().strip().split()))
# lstb = list(map(int,sys.stdin.readline().strip().split()))
#
# lsta.sort()
# lstb.sort(reverse=True)
# a = list(map(lambda a,b : a*b , lsta,lstb ))
# print(sum(a))

# 멀티탭 스케줄링
# import sys
#
# n,k = map(int,sys.stdin.readline().strip().split())
# lst = list(map(int,sys.stdin.readline().strip().split()))
# prilst = [0] * (k+1)
# tap= []
#
# for i in range(k):
#     prilst[lst[i]] = prilst[lst[i]] + 1
# init = 0
#
# while 1:
#     if len(tap) == (n+1) or init == k:
#         break
#
#     if lst[init] not in tap:
#         tap.append(lst[init])
#     init = init + 1
#
# if init == k:
#     cnt = 0
# else:
#     cnt = 1
#     for i in range(init,k):
#         prilst[lst[i]] = prilst[lst[i]] - 1
#         if lst[i] in tap:
#             continue
#         target = -1
#         pt = k
#         for j in range(n):
#             if prilst[tap[j]] < pt:
#                 target = j
#                 pt = prilst[tap[j]]
#
#         tap[target] = lst[i]
#         cnt = cnt + 1
#
# print(cnt)
# import sys
#
# n,k = map(int,sys.stdin.readline().strip().split())
# lst = list(map(int,sys.stdin.readline().strip().split()))
#
# prilst = [0] * (k+1)
# tap= []
# for i in range(k):
#     prilst[lst[i]] = prilst[lst[i]] + 1
#
# idx = 0
# while 1:
#     if len(tap) == n or idx == k:
#         break
#
#     if lst[idx] not in tap:
#         tap.append(lst[idx])
#     prilst[lst[idx]] = prilst[lst[idx]] - 1
#     idx = idx + 1
#
# cnt = 0
# for i in range(idx,k):
#     prilst[lst[i]] = prilst[lst[i]] - 1
#     if lst[i] in tap:
#         continue
#
#     fidx = -1
#     fval = -1
#     for j in range(n):
#         if prilst[tap[j]] == 0:
#             fidx = j
#             break
#         else:
#             if lst.index(tap[j],i)>fval:
#                 fval = lst.index(tap[j],i)
#                 fidx = j
#     tap[fidx] = lst[i]
#     cnt = cnt + 1
#
# print(cnt)

# 암호코드 스캔
# print(bin(int(codelst[0],16))) 코드 이진화

# coddic = {0:'2,1,1',1:'2,2,1',2:'1,2,2',3:'4,1,1',4:'1,3,2',5:'2,3,1',6:'1,1,4',7:'3,1,2',8:'2,1,3',9:'1,1,2'}
#
# for t in range(int(input().strip())):
#     n,m = map(int,input().strip().split())
#     codelst = []
#
#     for i in range(n):
#         stack = []
#         stack.extend(list(input().strip().strip('0')))
#
#         if len(stack) and not stack in codelst:
#                 codelst.append(stack)
#
#     result = []
#     sumv= 0
#     combinnumlst = []
#     for i in codelst:
#         numlst = []
#         bincode = bin(int(''.join(i), 16))
#         cnt1 = 0
#         cnt0 = 0
#         bincoderm = bincode.rstrip('0')
#         for j in bincoderm:         # 2진수 코드에서 1과 0의 갯수를 계산해서 리스트에 저장
#             if j == '1':
#                 cnt1 = cnt1 + 1
#
#                 if not cnt0 == 0:
#                     numlst.append(cnt0)
#                     cnt0 = 0
#
#             if j == '0':
#                 cnt0 = cnt0 + 1
#
#                 if not cnt1 == 0:
#                     numlst.append(cnt1)
#                     cnt1 = 0
#         else:
#             if j == '1':
#                 numlst.append(cnt1)
#             else:
#                 numlst.append(cnt0)
#
#         separatenumlst = []
#         for i in range(len(numlst)+1):
#             if i%32 :
#                 separatenumlst.append(numlst[i])
#             elif i%32==0 and i!=0:
#                 if separatenumlst not in combinnumlst:
#                     combinnumlst.append(separatenumlst)
#                 separatenumlst = []
#     coderesult = []
#     ckcode = 0
#     for finalnumlst in combinnumlst:
#         idx = 0
#         coderesult = []
#         ckcode = 0
#         for i in range(8):
#             if i == 0:
#                 a,b,c = finalnumlst[idx], finalnumlst[idx+1], finalnumlst[idx+2]
#                 div = min(a,b,c)
#                 ratio = f'{a//div},{b//div},{c//div}'
#                 for k,v in coddic.items():
#
#                     if ratio==v:
#                         coderesult.append(k)
#                         ckcode = ckcode + k*3
#
#                 idx = idx + 3
#             else:
#
#                 a, b, c, d = finalnumlst[idx], finalnumlst[idx + 1], finalnumlst[idx + 2], finalnumlst[idx + 3]
#                 div = min(a, b, c, d)
#                 ratio = f'{b//div},{c//div},{d//div}'
#                 for k,v in coddic.items():
#
#                     if ratio==v:
#                         coderesult.append(k)
#                         if i%2==0:
#                             ckcode = ckcode + k * 3
#                         else:
#                             ckcode = ckcode + k
#                 idx = idx + 4
#         if ckcode % 10 == 0 and coderesult not in result:
#             result.append(coderesult)
#             sumv = sumv + sum(coderesult)
#
#
#     print(f'#{t+1} {sumv}')

# 배열최소합
# def dfs(row,sumval):
#     if row == n:
#         result.append(sumval)
#         return
#
#     for i in range(n):
#         if not visited[i] and lst[row][i] != 1:
#             visited[i] = 1
#             dfs(row+1,sumval+lst[row][i])
#             visited[i] = 0
#
# for t in range(int(input())):
#     n = int(input())
#     lst = [list(map(int,input().split())) for _ in range(n)]
#     visited = [0]*n
#     result = []
#     dfs(0,0)
#     print(f'#{t+1} {min(result)}')

# 풍선팡
# di = [1,0,-1,0]
# dj = [0,1,0,-1]
#
# def cntballoon(r,c):
#     multi = lst[r][c]
#     if multi%2==0:
#         sumnum = 0
#     else:
#         sumnum = multi
#     for i in range(4):
#         for j in range(1,multi+1):
#             row = r + di[i]*j
#             col = c + dj[i]*j
#             if 0<=row<n and 0<=col<m:
#                 sumnum = sumnum + lst[row][col]
#
#     balloon[r][c] = sumnum
#
#
# for t in range(int(input())):
#     n,m = map(int,input().split())
#     lst = [list(map(int,input().split())) for _ in range(n)]
#     balloon = [[0]*m for _ in range(n)]
#
#     for i in range(n):
#         for j in range(m):
#             cntballoon(i,j)
#     result =[]
#     for i in balloon:
#         result.extend(i)
#
#     print(f'#{t+1} {max(result)}')

# 파리퇴치
# def flycatch(r,c):
#     sumN = ans[r][c]
#     for i in range(dis+1):
#         for j in range(dis+1-i):
#             if not (i==0 and j==0):
#                 sumN = sumN + ans[r+i][c+j] + ans[r-i][c-j]
#                 if i != 0 and j !=0:
#                     sumN = sumN + ans[r + i][c - j] + ans[r - i][c + j]
#     result.append(sumN)
#
# for t in range(int(input())):
#     n,m = map(int,input().split())
#     dis = m//2
#     ans = [[0]*(n+(dis*2)) for _ in range(n+(dis*2))]
#     lst = [list(map(int,input().split())) for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             ans[i+dis][j+dis] = lst[i][j]
#
#     result = []
#     for i in range(dis,n+dis):
#         for j in range(dis,n+dis):
#             flycatch(i,j)
#     print(f'#{t + 1} {max(result)}')

# # 스위치
# def switchpush(idx):
#     lst[idx] = 1-lst[idx]
#
# def maleswitch(idx):
#     for i in range(n):
#         if (i+1)%idx==0:
#             switchpush(i)
#
# def femaleswitch(idx):
#     idex = 0
#     while 1:
#
#         if lst[idx+idex]==lst[idx-idex] and 0<=idx-idex and idx+idex<n:
#             if idex == 0:
#                 switchpush(idx+idex)
#             else:
#                 switchpush(idx+idex)
#                 switchpush(idx-idex)
#         else:
#             break
#         idex=idex+1
#
#
#
# n = int(input())
# lst = list(map(int,input().split()))
# t = int(input())
# for _ in range(t):
#     s,i = map(int,input().split())
#     if s == 1:
#         maleswitch(i)
#     else:
#         femaleswitch(i-1)
# print(lst)

# 사과 먹기 게임 (DS A형 기출)
# def apple(y,x,r,c):     # r,c 타겟, x,y 현재좌표 , dir 0:오른 1:아래 2:왼 3:위
#     global cnt
#     dir = cnt % 4
#     if dir == 0:
#         if y<r and x<c:
#             cnt = cnt + 1
#         elif y<r and x>c:
#             cnt = cnt + 2
#         elif y>r and x>c:
#             cnt = cnt + 3
#         elif y>r and x<c:
#             cnt = cnt + 3
#     elif dir == 1:
#         if y < r and x > c:
#             cnt = cnt + 1
#         elif y > r and x > c:
#             cnt = cnt + 2
#         elif y > r and x < c:
#             cnt = cnt + 3
#         elif y < r and x < c:
#             cnt = cnt + 3
#     elif dir == 2:
#         if y > r and x > c:
#             cnt = cnt + 1
#         elif y > r and x < c:
#             cnt = cnt + 2
#         elif y < r and x < c:
#             cnt = cnt + 3
#         elif y < r and x > c:
#             cnt = cnt + 3
#     elif dir == 3:
#         if y > r and x < c:
#             cnt = cnt + 1
#         elif y < r and x < c:
#             cnt = cnt + 2
#         elif y < r and x > c:
#             cnt = cnt + 3
#         elif y > r and x > c:
#             cnt = cnt + 3
#
# for t in range(int(input())):
#     n = int(input())
#     m = [[] for _ in range(11)]
#     MAP = [list(map(int,input().split())) for _ in range(n)]
#
#     cnt = 0
#     x=y=0
#     for i in range(n):
#         for j in range(n):
#             if MAP[i][j] != 0:
#                 m[MAP[i][j]] = [i,j]
#     for i in m:
#         if len(i) == 2:
#             r,c = i
#             apple(y,x,r,c)
#             x = c
#             y = r
#
#     print(f'#{t+1} {cnt}')

# 장기 포(包) 게임 (DS A형 기출)
# def jangki(r,c,i):
#     if i == 3:
#         return
#     k = 1
#     ck = 0
#     while 1: # 오른쪽
#         if r+k==n:
#             break
#
#         if ck==1 and lst[r+k][c] == 1:
#             lst[r+k][c] = 0
#             if not [r+k,c] in result:
#                 result.append([r+k,c])
#             jangki(r+k,c,i+1)
#             lst[r + k][c] = 1
#             break
#
#         if ck == 0 and lst[r+k][c] == 1:
#             ck = 1
#
#         if ck == 1 and lst[r+k][c] == 0:
#             jangki(r+k,c,i+1)
#         k = k + 1
#
#     k = 1
#     ck = 0
#     while 1:  # 아래
#         if c + k == n:
#             break
#
#         if ck == 1 and lst[r][c + k] == 1:
#             lst[r][c + k] = 0
#             if not [r, c + k] in result:
#                 result.append([r, c + k])
#             jangki(r, c + k, i + 1)
#             lst[r][c + k] = 1
#             break
#
#         if ck == 0 and lst[r][c + k] == 1:
#             ck = 1
#
#         if ck == 1 and lst[r][c + k] == 0:
#             jangki(r, c + k, i + 1)
#         k = k + 1
#
#     k = -1
#     ck = 0
#     while 1:  # 왼쪽
#         if r + k < 0:
#             break
#
#         if ck == 1 and lst[r + k][c] == 1:
#             lst[r + k][c] = 0
#             if not [r + k, c] in result:
#                 result.append([r + k, c])
#             jangki(r + k, c, i + 1)
#             lst[r + k][c] = 1
#             break
#
#         if ck == 0 and lst[r + k][c] == 1:
#             ck = 1
#
#         if ck == 1 and lst[r + k][c] == 0:
#             jangki(r + k, c, i + 1)
#         k = k - 1
#
#     k = -1
#     ck = 0
#     while 1:  # 위쪽
#         if c + k < 0:
#             break
#
#         if ck == 1 and lst[r][c + k] == 1:
#             lst[r][c + k] = 0
#             if not [r, c + k] in result:
#                 result.append([r, c + k])
#             jangki(r, c + k, i + 1)
#             lst[r][c + k] = 1
#             break
#
#         if ck == 0 and lst[r][c + k] == 1:
#             ck = 1
#
#         if ck == 1 and lst[r][c + k] == 0:
#             jangki(r, c + k, i + 1)
#         k = k - 1
#
#
#     return
# for t in range(int(input())):
#     n = int(input())
#     lst = [list(map(int,input().split())) for _ in range(n)]
#     check=[[i,j] for i in range(n) for j in range(n) if lst[i][j]==2]
#
#     r,c = check[0]
#     result = []
#     jangki(r,c,0)
#     print(f'#{t+1} {len(result)}')

# # 풍선 사격 게임
# def dfs(c,pt,pript):
#     global result
#     if c == ball:
#         pt = pt + pript - 1
#         result = max(result,pt)
#         return
#
#     for i in range(1,ball+1-c):
#         point = lst[i-1]*lst[i+1]
#         tmp = lst.pop(i)
#         dfs(c+1,pt+point,tmp)
#         lst.insert(i,tmp)
#
# for t in range(int(input())):
#     n = int(input())
#     lst = list(map(int,input().split()))
#     cnt = 0
#     result = 0
#     for i in range(n):
#         ball = len(lst)
#         maxi = lst.index(max(lst))
#         if ball <= 9:
#             lst = [1] + lst + [1]
#             dfs(0, cnt, 0)
#             break
#
#         if maxi + 3 < ball:
#             if lst[maxi]*lst[maxi+2] >= lst[maxi+1]*lst[maxi+3]:
#                 cnt = cnt + lst[maxi]*lst[maxi+2]
#                 del lst[maxi+1]
#                 continue
#             else:
#                 cnt = cnt + lst[maxi+1]*lst[maxi+3]
#                 del lst[maxi + 2]
#                 continue
#         # elif maxi + 2 < ball:
#         #     cnt = cnt + lst[maxi] * lst[maxi + 2]
#         #     del lst[maxi + 1]
#         #     continue
#         elif maxi - 3 >= 0:
#             if lst[maxi]*lst[maxi-2] >= lst[maxi-1]*lst[maxi-3]:
#                 cnt = cnt + lst[maxi]*lst[maxi-2]
#                 del lst[maxi-1]
#                 continue
#             else:
#                 cnt = cnt + lst[maxi-1]*lst[maxi-3]
#                 del lst[maxi - 2]
#                 continue
#         # elif maxi - 2 >= 0:
#         #     cnt = cnt + lst[maxi] * lst[maxi - 2]
#         #     del lst[maxi - 1]
#         #     continue
#
#     print(f'#{t+1} {result} ')
#
# def dfs(c,pt,pript):
#     global result
#     if c == n:
#         pt = pt + pript - 1
#         result = max(result,pt)
#         return
#
#     for i in range(1,n+1-c):
#         point = lst[i-1]*lst[i+1]
#         tmp = lst.pop(i)
#         dfs(c+1,pt+point,tmp)
#         lst.insert(i,tmp)
#
#
# for t in range(int(input())):
#     n = int(input())
#     lst = [1]+list(map(int,input().split()))+[1]
#     rng = n+2
#     result = 0
#     dfs(0,0,0)
#     print(f'#{t + 1} {result}')

# import sys
# l =int(sys.stdin.readline().strip())
# n =int(sys.stdin.readline().strip())
# audlst = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
# hopemax = -1
# realmax = -1
# ans1 = 0
# ans2 = 0
# ck = [0]*(l+1)
# for i in range(n):
#     b,e = audlst[i]
#     cnt = 0
#     if e-b > hopemax:
#         ans1 = i+1
#         hopemax = e-b
#     for j in range(b,e+1):
#         if ck[j]==0:
#             ck[j] = 1
#             cnt = cnt + 1
#     if cnt>realmax:
#         ans2 = i + 1
#         realmax = cnt
# print(ans1)
# print(ans2)

# import sys
# n = int(sys.stdin.readline().strip())
# lst = list(map(int,sys.stdin.readline().strip().split()))
# b,c = map(int,sys.stdin.readline().strip().split())
# stulst = []
# for i in lst:
#     ans = i - b
#     if ans<0:
#         ans = 0
#     stulst.append(ans)
# stulst2 = list(map(lambda x: x/c,stulst))
# ans = n
# for i in stulst2:
#     if i%1==0:
#         ans = ans + int(i)
#     else:
#         ans = ans + int(i) + 1
# print(ans)

# 지역구 나누기
# from collections import deque
# def seperate(c):
#     cproute = route.copy()
#     cproute.sort()
#     stack.add(''.join(cproute))
#
#
#     for i in lst[c]:
#         if not visited[i]:
#             route.append(str(i))
#             visited[i] = 1
#             seperate(i)
#             visited[i] = 0
#             route.pop()
#
#     return
#
# def bfs(c):
#     q = deque()
#     q.append(c)
#
#     while q:
#         v = q.popleft()
#         visited[v] = 1
#         for i in lst[v]:
#             if not visited[i]:
#                 q.append(i)
#
#
# for t in range(int(input())):
#     n = int(input())
#     lst= [[] for _ in range(n)]
#
#     for i in range(n):
#         cntlst = list(map(int,input().split()))
#         for j in range(n):
#             if cntlst[j] == 1:
#                 lst[i].append(j)
#
#     ptlst = list(map(int,input().split()))
#     totpt = sum(ptlst)
#     stack = set([])
#     for i in range(n):
#         route = []
#         visited = [0] * n
#         route.append(str(i))
#         visited[i] = 1
#         seperate(i)
#     ans = float('inf')
#
#     for i in stack:
#         nlst = [i for i in range(n)]
#         sum1 = 0
#         visited = [0] * n
#         for j in i:
#             num = int(j)
#             sum1 = sum1 + ptlst[num]
#             nlst.remove(num)
#             visited[num] = 1
#         if len(nlst) != 0:
#             bfs(nlst[0])
#         cknum = ''.join(list(map(str,nlst)))
#         if 0 not in visited:
#             sum2 = totpt-sum1
#             ans = min(ans,abs(sum1 - sum2))
#         else:
#             continue
#         if ans == 0:
#             break
#
#     print(f'#{t+1} {ans}')

# 마법의 물뿌리개 (DS A형 기출) 11,18,20
# for t in range(int(input())):
#     n = int(input())
#     tlst = list(map(int,input().split()))
#     tmax = max(tlst)
#     tdif = list(map(lambda x : tmax-x,tlst))
#     cnt = 0
#     tdif4up = len(tdif)-(tdif.count(0)+tdif.count(1)+tdif.count(2)+tdif.count(3))
#     for i in range(len(tdif)):
#         while tdif[i] > 2:
#             tdif[i]  = tdif[i] -3
#             cnt = cnt + 2
#     tdif.sort()
#     tdif1 = tdif.count(1)
#     tdif2 = tdif.count(2)
#     if tdif1 == tdif2:
#         cnt = cnt + tdif1*2
#         print(f'#{t + 1} {cnt}')
#         continue
#     elif tdif1 < tdif2:
#         tdif2 = tdif2 - tdif1
#         cnt = cnt + tdif1*2
#         if tdif2%3==0:
#             tritdif2 = tdif2//3
#             cnt = cnt + 4*tritdif2
#         elif tdif2%3==1:
#             tritdif2 = tdif2 // 3
#             cnt = cnt + 4 * tritdif2 + 2
#         elif tdif2%3==2:
#             tritdif2 = tdif2 // 3
#             cnt = cnt + 4 * tritdif2 + 3
#     else:
#         tdif1 = tdif1 - tdif2
#         cnt = cnt + tdif2 * 2
#         if tdif1 == 1:
#             cnt = cnt + 1
#         else:
#             if tdif1%3==0:
#                 fndtrip = tdif1//3
#             else:
#                 fndtrip = tdif1 // 3 + 1
#             tdif4 = min(fndtrip,tdif4up)
#             tdif1 = tdif1 - tdif4
#             tdif2 =tdif4*2
#             cnt = cnt - tdif4*2
#             i = 1
#             while tdif1+tdif2>0:
#                 water = i%2
#                 if water == 1 and tdif1>0:
#                     tdif1 = tdif1 - 1
#                     cnt = cnt + 1
#                 elif water == 0 and tdif2>0:
#                     tdif2 = tdif2 - 1
#                     cnt = cnt + 1
#                 elif water == 0 and tdif2==0:
#                     cnt = cnt + 1
#                 else:
#                     cnt = cnt + 1
#                 i = i + 1
#
#
#     print(f'#{t+1} {cnt}')

# 주사위 굴리기
# import sys
# di = [0,1,-1,0,0]
# dj = [0,0,0,-1,1]
#
# def movedice(dir):
#     if dir == 1:
#         dice[1][0],dice[1][1],dice[1][2],dice[3][0] = dice[1][1],dice[1][2],dice[3][0],dice[1][0]
#     elif dir == 2:
#         dice[1][0],dice[1][1],dice[1][2],dice[3][0] = dice[3][0],dice[1][0],dice[1][1],dice[1][2]
#     elif dir == 3:
#         dice[0][0],dice[1][1],dice[2][0],dice[3][0] = dice[1][1],dice[2][0],dice[3][0],dice[0][0]
#     elif dir == 4:
#         dice[0][0],dice[1][1],dice[2][0],dice[3][0] = dice[3][0],dice[0][0],dice[1][1],dice[2][0]
#
#
# n,m,x,y,k = map(int,sys.stdin.readline().strip().split())
# lst = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
# movelst = list(map(int,sys.stdin.readline().strip().split()))
# dice = [[0],[0,0,0],[0],[0]]
# cp = [x,y]
#
# for i in movelst:
#     if 0<=cp[0]+dj[i]<n and 0<=cp[1]+di[i]<m:
#          cp[0]=cp[0]+dj[i]
#          cp[1]=cp[1]+di[i]
#          movedice(i)
#          # if dice[1][1] == 0 and lst[cp[0]][cp[1]]!=0:
#          if dice[1][1] != 0 and lst[cp[0]][cp[1]]==0:
#             lst[cp[0]][cp[1]]=dice[1][1]
#          elif lst[cp[0]][cp[1]]!=0:
#             dice[1][1],lst[cp[0]][cp[1]]=lst[cp[0]][cp[1]],0
#          print(dice[3][0])

# 산악 구조 로봇 (DS A형 기출 Upgrade)
# def rdifpt(r,c):
#     if lst[r][c] > lst[r][c-1]:
#         pt = ptlst[r][c - 1] +(lst[r][c] - lst[r][c-1])*2
#     elif lst[r][c] < lst[r][c-1]:
#         pt = ptlst[r][c-1]
#     elif lst[r][c] == lst[r][c-1]:
#         pt = ptlst[r][c - 1] + 1
#
#     return pt
# def ldifpt(r,c):
#     pt = float('inf')
#     if c+1<n:
#         if lst[r][c] > lst[r][c+1]:
#             pt = ptlst[r][c + 1] +(lst[r][c] - lst[r][c+1])*2
#         elif lst[r][c] < lst[r][c+1]:
#             pt = ptlst[r][c+1]
#         elif lst[r][c] == lst[r][c+1]:
#             pt = ptlst[r][c + 1] + 1
#
#     return pt
#
# def ddifpt(r,c):
#
#     if lst[r][c] > lst[r-1][c]:
#         pt = ptlst[r-1][c] +(lst[r][c] - lst[r-1][c])*2
#     elif lst[r][c] < lst[r-1][c]:
#         pt = ptlst[r-1][c]
#     elif lst[r][c] == lst[r-1][c]:
#         pt = ptlst[r-1][c] + 1
#
#     return pt
#
# for t in range(int(input())):
#     n,m = map(int,input().split())
#     lst = [list(map(int,input().split())) for _ in range(n)]
#     ptlst = [[0]*(n+1) for _ in range(n+1)]
#     axlst =[]
#     aylst =[]
#     bxlst =[]
#     bylst =[]
#     clst =[]
#
#     for i in range(m):
#         ax,ay,bx,by,c = map(int,input().split())
#         axlst.append(ax-1)
#         aylst.append(ay-1)
#         bxlst.append(bx-1)
#         bylst.append(by-1)
#         clst.append(c)
#
#     for i in range(n):
#         for j in range(n):
#             if i==0 and j == 0:
#                 ptlst[i][j] = 0
#             elif i == 0:
#                 ptlst[i][j] = rdifpt(i,j)
#             elif j==0:
#                 ptlst[i][j] = ddifpt(i,j)
#
#     for i in range(1,n):
#         for j in range(i,n):
#             for k in range(i,n):
#                 if j == i or k == i:
#
#                     for l in range(m):
#                         if j == bxlst[l] and k == bylst[l]:
#                             ptlst[j][k] = min(ddifpt(j,k),rdifpt(j,k),ldifpt(j,k),ptlst[axlst[l]][aylst[l]]+clst[l])
#                         else:
#                             ptlst[j][k] = min(ddifpt(j,k),rdifpt(j,k),ldifpt(j,k))
#
#     print(ptlst)
#     print(f'#{t+1} {ptlst[n-1][n-1]}')

# 영식이와 친구들
# import sys
# m,n,l = map(int,sys.stdin.readline().split())
# cntball = [0]*m
# v = 0
# ans = -1
# while 1:
#     if n in cntball:
#         break
#     ballpos = v%m
#     cntball[ballpos] += 1
#     ans = ans + 1
#     if cntball[ballpos]%2 == 1:
#         v = v + l
#     else:
#         v = v - l
# print(ans)

# 직사각형
#
# import sys
# for _ in range(4):
#
#     x1,x2,x3,x4,y1,y2,y3,y4 = map(int,sys.stdin.readline().strip().split())
#     if y3<x1 or x3<y1 or y4<x2 or x4<y2: # 첫 사각형의 시작점(왼쪽아래) 보다 두번째 사각형 끝점 (오른쪽 위) 크거나 그 반대일 경우 접점이 없다
#         ans = 'd'
#     elif (x1==y3 and x2==y4) or (y1==x3 and y2==x4) or (x4==y2 and x1==y3) or (y4==x2 and y1==x3):
#         ans = 'c'
#     elif x1==y3 or y1==x3 or x2==y4 or y2==x4:
#         ans = 'b'
#     else:
#         ans = 'a'
#
#     print(ans)



# memo = {}
#
#
# def shot(lst):
#     state = ','.join(map(str, lst))
#     if state in memo:
#         return memo[state]
#
#     EA = len(lst)
#     if EA == 1:
#         return lst[0]
#
#     max_score = 0
#     for i in range(EA):
#         temp_score = 0
#         if i == 0:
#             temp_score += lst[1]
#         elif i == EA - 1:
#             temp_score += lst[EA - 2]
#         else:
#             temp_score += (lst[i - 1] * lst[i + 1])
#
#         temp = lst[:i] + lst[i + 1:]
#         curr_score = temp_score + shot(temp)
#         max_score = max(max_score, curr_score)
#
#     memo[state] = max_score
#     return max_score
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     result = shot(lst)
#     print(f"#{tc} {result}")

# import sys
# input = sys.stdin.readline
# n = int(input())
# lst = [list(map(str,input().strip().split())) for _ in range(n)]
# lst.sort()
# wordlen = 1
# preword='A'
# cnt = 0
# for i in range(51):
#     # if cnt == n:
#     #     break
#     for j in lst:
#         if j == preword:
#             cnt +=1
#             continue
#         if i == len(j[0]):
#             print(j[0])
#             preword = j
#             cnt +=1

import sys
input = sys.stdin.readline
k,n = map(int,input().strip().split())
lst = [int(input().strip()) for _ in range(k)]
minv = 0
maxv = max(lst)
while minv<=maxv:
    divpt = (maxv+minv)//2
    lst1 = list(map(lambda j: j // divpt, lst))
    if sum(lst1) >= n:
        minv = divpt + 1
    else:
        maxv = divpt - 1
print(maxv)
# while 1:
#     divn = sum(lst)//i
#     lst1 =list(map(lambda j : j//divn,lst))
#     if sum(lst1) >= n:
#         epos = sum(lst)//i
#         spos = sum(lst)//(i-1)
#         break
#     i += 1
# while 1:
#     ans = (epos + spos)//2
#     lst1 =list(map(lambda j : j//ans,lst))
#     lst2 =list(map(lambda j : j//(ans-1),lst))
#     if sum(lst1) < n:
#         if sum(lst2)==n:
#             result = ans - 1
#             break
#         spos = ans + 1
#     else:
#         epos = ans - 1
# print(result)