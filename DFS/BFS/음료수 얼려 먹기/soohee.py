from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

##### dfs

# def dfs(graph, x, y):
#     if ( 0 <= x and x < n ) and (0 <= y and y < m ):
#         if graph[x][y] == 0:
#             graph[x][y] = 2
#             dfs(graph, x-1, y)
#             dfs(graph, x+1, y)
#             dfs(graph, x, y-1)
#             dfs(graph, x, y+1)
#             return True
#     return False
    

# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(graph, i , j):
#             cnt += 1
# print(cnt)


##### bfs

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 

def bfs(x, y): 
    cnt = 0
    queue = deque()
    queue.append((x,y)) 
    while queue: 
        x, y = queue.popleft() 
        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or  nx >= n or ny < 0  or ny >= m: 
                continue 
            if graph[nx][ny] == 1: 
                continue 
            if graph[nx][ny] == 0: 
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny)) 
    return cnt 
print(bfs(0, 0))

    