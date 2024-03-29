from collections import deque


def merge(l, r):
    result = []
    global cnt

    if l[-1] > r[-1]:
        cnt += 1

    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                result.append(l.popleft())
            else:
                result.append(r.popleft())
        elif len(l) > 0:
            result.append(l.popleft())
        elif len(r) > 0:
            result.append(r.popleft())

    return result


def mergesort(lst, n):
    if n == 1:
        return lst
    mid = n // 2
    divl = lst[0:mid]
    divr = lst[mid:n]
    l = deque()
    r = deque()
    l.extend(mergesort(divl, len(divl)))
    r.extend(mergesort(divr, len(divr)))

    return merge(l, r)


for t in range(int(input().strip())):
    n = int(input().strip())
    lststart = list(map(int, input().strip().split()))
    cnt = 0
    listresult = mergesort(lststart, n)
    print(f'#{t + 1} {listresult[n // 2]} {cnt}')

