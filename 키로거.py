import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input().strip())):
    frontp = deque()
    backp = deque()
    lst = deque(input().strip())
    while lst:
        action = lst.popleft()
        if action == '-':
            if len(frontp)==0:
                continue
            frontp.pop()
            continue
        elif action == '<':
            if len(frontp) == 0:
                continue
            tmpchar = frontp.pop()
            backp.append(tmpchar)
            continue
        elif action == '>':
            if len(backp)==0:
                continue
            tmpchar = backp.pop()
            frontp.append(tmpchar)
            continue
        else:
            frontp.append(action)
    print(''.join(list(frontp)),end='')
    print(''.join(list(backp)[::-1]))
