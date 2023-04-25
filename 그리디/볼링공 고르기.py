import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nlist = list(map(int, input().split()))

cnt = 0
# for i in range(n):
#     for j in range(i, n):
#         if nlist[i] != nlist[j]:
#             cnt += 1
arr = [0] * 11
for x in nlist:
    arr[x] += 1

for i in range(1, m+1):
    n -= arr[i]
    cnt += arr[i] * n

print(cnt)