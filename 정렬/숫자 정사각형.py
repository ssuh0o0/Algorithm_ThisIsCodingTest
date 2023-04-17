import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().strip())))

number = n if n < m else m

for num in range(number-1, -1, -1):
    for i in range(n-num):
        for j in range(m-num):
            if nlist[i][j] == nlist[i+num][j] == nlist[i][j+num] == nlist[i+num][j+num]:
                print((num+1)*(num+1))
                exit(0)



