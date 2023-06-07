import sys

n = int(input())
v = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    if line[-1] == -1:
        line.pop()  # -1 제거
    v.append(line)

v.sort()

for i in range(n):
    print(*v[i])
