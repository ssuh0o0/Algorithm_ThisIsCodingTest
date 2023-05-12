import sys
input = sys.stdin.readline 
m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(m)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(y, x):
    if y == m - 1 and x == n - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= ny < m and 0 <= nx < n:
            if graph[y][x] > graph[ny][nx]:
                cnt += dfs(ny, nx)

    graph[y][x] = cnt
    return graph[y][x] 


print(dfs(0,0))