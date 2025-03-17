t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    if b ** 2 > a:
        print("NO")
    elif a%2 != b%2:
        print("NO")
    else:
        print("YES")