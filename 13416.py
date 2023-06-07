T = int(input())

for i in range(T):
    Total = 0
    N = int(input())
    for j in range(N):
        A, B, C = map(int, input().split())
        max_val = max(A, B, C)
        if max_val > 0:
            Total += max_val
    print(Total)
