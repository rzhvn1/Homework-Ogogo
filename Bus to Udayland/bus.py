row = int(input())

lst_str = []
i = 0
while i < row:
    string = input()
    lst_str.append(string)
    i += 1

count = 0
new_lst = []
check = 'NO'
for j in lst_str:
    if 'OO' not in j:
        new_lst.append(j)
    elif count == 1:
        new_lst.append(j)
        continue
    else:
        check = 'YES'
        print(check)
        count += 1
        j = j.replace('OO', '++',1)
        new_lst.append(j)

if check == 'NO':
    print(check)
else:
    for k in new_lst:
        print(k)
