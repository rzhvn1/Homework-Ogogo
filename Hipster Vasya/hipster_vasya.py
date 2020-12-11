socks = list(map(int,input().split()))
a = socks[0]
b = socks[1]

count_fash = min(a, b)
count_notfash = (a - min(a, b) + b - min(a, b))//2

print(count_fash, count_notfash)

