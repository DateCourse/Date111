n = int(input())
s = input()

for k in range(1, n - 1):
    for j in range(k + 1, n - k + 1):
        for i in range(k, n - j + 1):
            if s[i:i+j] == s[i-k:i-k+j]:
                print("YES")
                print(s[i:i+j])
                exit()
print("NO")
