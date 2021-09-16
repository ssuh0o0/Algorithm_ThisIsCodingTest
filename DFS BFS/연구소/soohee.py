n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

cnt = 0
def dfs(graph, x, y):

    if ( 0 <= x and x < n ) and (0 <= y and y < m ):
        if graph[x][y] == 0:
            graph[x][y] = 2
            dfs(graph, x-1, y)
            dfs(graph, x+1, y)
            dfs(graph, x, y-1)
            dfs(graph, x, y+1)
            return True
    return False
    
print(cnt)