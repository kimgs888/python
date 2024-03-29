import sys
n = int(sys.stdin.readline().strip())
lst = [int(sys.stdin.readline().strip()) for _ in range(n)]
lst.sort()
for i in lst:
    print(i)