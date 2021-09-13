import sys
from collections import deque
 
input = sys.stdin.readline

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())


graph = [[] for _ in range(n + 1)]  # 도로 연결 정보 담는 그래프 초기화
distance = [-1] * (n + 1)  # 최단 거리 초기화
distance[x] = 0  # 출발 노드까지 거리 0으로 초기화


# 그래프 만들어주기
for _ in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    

que = deque([x])
while que:
    now = que.popleft()
    for next_node in graph[now]:
        # 방문 전이라면 
        if distance[next_node] == -1:

            # 최단거리 +1
            distance[next_node] = distance[now] + 1 
            que.append(next_node) 

print(distance)

# k값이 존재하는지 확인후 출력
for i in range(n+1):
    if distance[i] == k:
        print(i)

# 최단거리 없을 경우
if k not in distance:
    print(-1)