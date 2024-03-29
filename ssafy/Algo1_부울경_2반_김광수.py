for t in range(int(input())):
    ckbit, numlst = map(str,input().split())
    if ckbit == '24': # 이진수이면
        changeint = int(numlst,2)
        result = hex(changeint)[2:].upper() #대문자로
        while 1:
            if len(result) == 6:
                break
            else:
                result = '0'+ result
    elif ckbit == '6': # 십육진수이면
        changeint = int(numlst,16)
        result = bin(changeint)[2:]
        while 1:
            if len(result) == 24: #길이 맞추기
                break
            else:
                result = '0'+ result
    print(f'#{t+1} {result}')