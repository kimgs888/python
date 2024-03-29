import sys
def check():
    global ans
    for i in range(4):
        if diclst[cklst[i]] >= cklenlst[i]:
            continue
        else:
            return
    ans += 1

def rmdiclst(i):
    diclst[lst[i]] -= 1

def adddiclst(i):
    diclst[lst[i]] += 1

s,p = map(int,sys.stdin.readline().strip().split())
lst = sys.stdin.readline().strip()
cklenlst = list(map(int,sys.stdin.readline().strip().split()))
cklst = ['A','C','G','T']
ans = 0
spt,ept = 0,p-1
diclst = {'A':0,'C':0,'G':0,'T':0}

for i in range(spt, ept + 1):
    adddiclst(i)

while 1:
    flag = 0
    check()
    rmdiclst(spt)
    spt += 1
    ept += 1
    if ept == s:
        break
    adddiclst(ept)

print(ans)