from random import randint

players = 10
names = ['urmatik', 'beksich', 'aziretich', 'businesswman', 'erjanchik', 'ataichik', 'rasulchik',
         'rusik', 'sanjarchik', 'saidchik']
print(len(names))
n_names = []
n_value = []
i = 0


def twenty_one(names, players: int):
    i = 0
    while i < players:
        print(f'Играет {names[i]}')
        two_cards = randint(2, 11) + randint(2, 11)
        print(two_cards)
        if two_cards > 21:
            break
        check = input('One more? да/нет')
        while check == 'да':
            two_cards = two_cards + randint(2, 11)
            print(two_cards)
            if two_cards > 21:
                break
            check = input('One more? да/нет')

        if two_cards > 21:
            two_cards = 0
        if two_cards > 0:
            n_names.append(names[i])
            n_value.append(two_cards)
        # Придумать алгоритм на удаление из names

        print(f'У игрока {names[i]} {two_cards} очков!')
        i += 1

twenty_one(names, 10)






