def qsort(lst, l, r):
    if l < r:
        v = lst[l]
        i = l
        j = r
        while i <= j:
            while i <= j and lst[i] <= v:
                i += 1
            while lst[j] >= v and j >= i:
                j -= 1
            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
        lst[l], lst[j] = lst[j], lst[l]
        qsort(lst, l, j - 1)
        qsort(lst, j + 1, r)
    return lst

for t in range(int(input().strip())):
    n = int(input().strip())
    lststart = list(map(int, input().strip().split()))
    print(f'#{t+1} {qsort(lststart, 0, n - 1)[n//2]}')