n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    # 얼음판 벗어나는 경우
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 얼릴수 있는공간 0 이 나오면
    if graph[x][y] == 0:

        # 얼린다 1로 바꿈
        graph[x][y] = 1

        # 왼오상하 얼릴수 있는지 확인
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False



count = 0
for x in range (n):
    for y in range (m):
        if dfs(x, y) == True:

            # True가 나온 갯수 반환
            count += 1

print(count)   