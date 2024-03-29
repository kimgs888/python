# dic = {'aaa':1,'ddd':3,'ccc':2}
# newdic = sorted(dic.items(),key= lambda i : i[1])
# print(newdic)
import sys
input = sys.stdin.readline
k,l = map(int,input().strip().split())
enroldic = {}

for i in range(l):
    id = input().strip()
    enroldic[id] = i
newdic = sorted(enroldic.items(),key= lambda i : i[1])
for i in range(k):
    if i+1>len(newdic):
        break
    print(newdic[i][0])