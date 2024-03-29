# import sys
#
# dp = [[0 for _ in range(1001)] for _ in range(1001)]
# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()
# la,lb = len(a),len(b)
# for i in range(1,la+1):
#     for j in range(1,lb+1):
#         if a[i-1]==b[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#
# print(dp[la][lb])
# 재귀적
def lcs(x,y):
    m,n = len(x),len(y)
    if m == 0 or n == 0:
        return 0
    else:
        if x[-1] == y[-1]:
            return lcs(x[:(m-1)],y[:(n-1)]) + 1
        else:
            return max(lcs(x[:m],y[:(n-1)]),
                       lcs(x[:(m-1)],y[:n]))
# 요소 찾기
def lcs(x,y):
    x,y = ['']+x,['']+y
    m,n = len(x),len(y)
    c = [[0 for _ in range(n)] for _ in range(m)]
    b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            else:
                c[i][j] = max(c[i][j-1],c[i-1][j])
                b[i][j] = 2 if (c[i][j-1]>c[i-1][j]) else 3
    return c,b

def get_lcs(i,j,b,x):
    if i == 0 or j == 0:
        return ''
    else:
        if b[i][j] ==1:
            return get_lcs(i-1,j-1,b,x) + x[i]
        elif b[i][j] == 2:
            return get_lcs(i,j-1,b,x)
        elif b[i][j] == 3:
            return get_lcs(i-1,j,b,x)