number = list(map(int, input().split()))

n1 = str(number[0])
n2 = number[1]

i = 0
while i < n2:
    if n1[-1] == '0':
        n1 = int(n1)
        n1 = n1 // 10
        n1 = str(n1)
    else:
        n1 = int(n1)
        n1 -= 1
        n1 = str(n1)


    i += 1

print(int(n1))

