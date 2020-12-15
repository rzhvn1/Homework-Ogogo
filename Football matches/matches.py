team_num = int(input())

i = 0
lst_colors = []
while i < team_num:
    colors = list(map(int, input().split()))
    lst_colors.append(colors)
    i += 1
count = 0
for j in lst_colors:
    for k in lst_colors:
        if j[0] == k[1]:
            count += 1

print(count)
