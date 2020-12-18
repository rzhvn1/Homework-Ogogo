num = int(input())
i = 0
while i < num:
    count = 0
    lst1 = list(map(int,input().split()))
    a = lst1[0]
    b = lst1[1]
    n = lst1[2]
    i += 1
    while max(a,b) < n + 1:
        if a < b:
            a += b
        else:
            b += a
        count += 1
    print(count)
