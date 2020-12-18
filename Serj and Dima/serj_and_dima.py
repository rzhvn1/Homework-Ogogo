n = int(input('Please input how many cards on the table: '))
cards = list(map(int, input('Please input the values on the cards: ').split()))
print(cards)
serj = 0
dima = 0
i = 0
while i < n:
    scale = max(cards[0], cards[-1])
    if i % 2 == 0:
        serj += scale
    else:
        dima += scale
    i += 1
    cards.remove(scale)

print(serj, dima)

