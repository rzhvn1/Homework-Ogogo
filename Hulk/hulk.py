levels = int(input())
string = 'I hate it'
i = 1
while i <= levels:
    if i == 1:
        pass
    elif i % 2 == 0:
        string = string.replace('it', 'that I love it')
    elif i % 2 != 0:
        string = string.replace('it', 'that I hate it' )
    i += 1

print(string)