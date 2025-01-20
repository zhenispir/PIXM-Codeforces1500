t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    x, y = 0, 0
    flag = False
    for j in s:
        if j == 'L':
            x -= 1
        elif j == 'R':
            x += 1
        elif j == 'D':
            y -= 1
        elif j == 'U':
            y += 1
        
        if x == 1 and y == 1:
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')