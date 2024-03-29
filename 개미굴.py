import sys

def anthill(v,r,privroom):
    print('--'*r + v)
    underroom = privroom +'--' + v
    if not underroom in antdic.keys():
        return
    else:
        ulst = list(antdic[underroom])
        ulst.sort()
        for ant in ulst:
            anthill(ant,r+1,underroom)


n = int(sys.stdin.readline().strip())
antdic = {}
for _ in range(n):
    lst = list(map(str,sys.stdin.readline().strip().split()))
    for i in range(1,len(lst)):
        if i == 1:
            if not '0' in antdic.keys():
                antdic['0'] = set(lst[i].split())
            else:
                antdic['0'].add(lst[i])
        else:
            momant = ''
            for j in range(1,i):
                momant += '--'+lst[j]
            if not momant in antdic.keys():
                antdic[momant] = set(lst[i].split())
            else:
                antdic[momant].add(lst[i])
rootants = list(antdic['0'])
rootants.sort()
for i in rootants:
    anthill(i,0,'')