<<<<<<< HEAD
# 인접 행렬 BFS
graph = [
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
]

visited = [0] * 5

def bfs(start):

    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in range(5):
            if graph[now][to] == 0:
                continue

            if visited[to]:
                continue

            visited[to] = 1
            queue.append(to)

bfs(0)


=======
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph,1,visited)
>>>>>>> 875a0b2b2d1657fe9228397c098597f5784f6414
