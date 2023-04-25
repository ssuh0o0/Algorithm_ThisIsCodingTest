import sys
input = sys.stdin.readline
n =  int(input())
nlist = list(map(int, input().split()))
nlist.sort()

target = 1
for x in nlist:
    if target < x:
        break
    target += x

print(target)