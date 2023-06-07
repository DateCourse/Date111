T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    x = 0
    y = 0

    if N % H == 0:
        x = N // H
        y = H * 100
    else:
        x = N // H + 1
        y = N % H * 100
    print(y+x)