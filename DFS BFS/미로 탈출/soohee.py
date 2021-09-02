from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1, 0, -1, 0 ] # 오른쪽 아래 왼쪽 위
dy = [0, 1, 0, -1] 

def bfs(x, y): 
    cnt = 1
    visited = [[0] * n for _ in range(m) ] 
    queue = deque()
    queue.append((x,y)) 
    while queue: 
        x, y = queue.popleft() 
        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or  nx >= n or ny < 0  or ny >= m: 
                continue 
            if graph[nx][ny] == 0: 
                continue 
            if graph[nx][ny] == 1 and visited[nx][ny] == 0 : 
                graph[nx][ny] = cnt
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny)) 
    return cnt 
print(bfs(0, 0))