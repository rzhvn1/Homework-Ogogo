num = int(input())

i = 0
while i < num:
    string = input()
    if len(string) >= 2:
        print(string[::2] + string[-1])
    i += 1




