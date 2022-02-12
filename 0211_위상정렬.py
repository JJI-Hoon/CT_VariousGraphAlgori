from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)  # 진입차수
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


# 위상정렬함수
def topology_sort():
    result = []
    q = deque()  # 큐 기능을 위한 deque 라이브러리

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
