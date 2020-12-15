string = input()

if not string[0].istitle() and string[1:].isupper():
    print(string.swapcase())
elif string.isupper():
    print(string.swapcase())
elif len(string) > 1 and string.islower():
    print(string)
elif len(string) == 1 and string.islower():
    print(string.swapcase())
else:
    print(string)