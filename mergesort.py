#
# def merge(l, r):
#     result = []
#     i = j = 0
#
#     while i < len(l) and j < len(r):
#         if l[i] < r[j]:
#             result.append(l[i])
#             i += 1
#         else:
#             result.append(r[j])
#             j += 1
#
#     result.extend(l[i:])
#     result.extend(r[j:])
#     return result
#
# def mergesort(lst):
#     n = len(lst)
#     if n <= 1:
#         return lst
#     mid = n // 2
#     divl = lst[:mid]
#     divr = lst[mid:]
#
#     l = mergesort(divl)
#     r = mergesort(divr)
#     print(l,r)
#     return merge(l, r)
#
# # 테스트
# arr = [12, 11, 13, 5, 6, 7]
# print("주어진 배열:", arr)
# print("정렬된 배열:", mergesort(arr))

def mergesort(lst):
    global cnt


    if len(lst) < 2:
        return lst

    # 분할
    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])


    # merging (합치는 부분)

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            #작은 값을 추가하는 이유는 리스트가 정렬되어있기 때문에 리스트를 합칠때 작은값부터 넣어주기 위해서
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    # 이미 정렬 시킨 부분리스트에서 남은 요소들 합쳐주는 과정

    result = result + left[i:]
    result = result + right[j:]

    if left[-1] > right[-1]:
        cnt = cnt + 1

    return result

T = int(input())

for t in range(T):
    N = int(input())
    lst = list(map(int,input().split()))

    # print(N,lst)
    cnt = 0

    sortedList = mergesort(lst)
    # print(sortedList)
    result = sortedList[N//2]
    print(f"#{t+1} {result} {cnt}")