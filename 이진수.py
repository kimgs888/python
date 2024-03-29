for t in range(int(input())):
    strlen, hxstr = map(str,input().split())
    result = bin(int(hxstr,16))
    result = str(result[2:])
    while 1:
        if len(result)%4==0:
            break
        else:
            result = '0'+result

    print(f'#{t+1} {result}')