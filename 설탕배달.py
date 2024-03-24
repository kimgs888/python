import sys
n = int(sys.stdin.readline().strip())
suger5 = 5
suger3 = 3
init5 = n//suger5
ans = -1
while 1:
    tot5 = init5 * 5
    if (n-tot5)%3 == 0:
        ans = init5 + (n-tot5)//3
        break
    init5 -= 1
    if init5<0:
        break

print(ans)