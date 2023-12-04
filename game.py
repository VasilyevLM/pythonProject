import random

damage = None
hit = random.choice([True, False])
warrior1 = ['Первый воин', 100]
warrior2 = ['Второй воин', 100]
active = None


def kick():
    global active #использовать глобальные переменные - плохая практика (попробуй без них).
    global warrior1 #использовать глобальные переменные - плохая практика (попробуй без них).
    global warrior2 #использовать глобальные переменные - плохая практика (попробуй без них).
    global damage #использовать глобальные переменные - плохая практика (попробуй без них).
    damage = random.randint(1, 20)
    active = random.choice([warrior1, warrior2])
    if active == warrior1: #повторение кода (стр.18-24 и 26-32) можно вынести в функцию.
        name = active[0]
        hp = active[1]
        hp -= damage
        print(name, 'получает', damage, 'урона, у него остается', hp, 'hp.')
        active[1] = hp
        warrior1 = active
        return warrior1
    elif active == warrior2: #повторение кода (стр.18-24 и 26-32) можно вынести в функцию.
        name = active[0]
        hp = active[1]
        hp -= damage
        print(name, 'получает', damage, 'урона, у него остается', hp, 'hp.')
        active[1] = hp
        warrior2 = active
        return warrior2


print('Добро пожаловать на бои без правил! Вас ждут захватывающее зрелище! Два опытных сильнейших воина сойдутся в смертельном бою. \nПобедителем станет только один из них. Вы готовы попытать счастья и сделать свою ставку? \nКоэффициент на победу х10!')
bet = int(input('Сколько $ вы готовы поставить?'))
print('Ваша ставка $', bet, 'принята!')


if hit:
    print('Драка состоялась!')
    kick()
    while warrior1[1] > 0 and warrior2[1] > 0:
        kick()

    if warrior1[1] > warrior2[1]:
        win_sum = bet * 10
        print('Победил первый воин, ваш выигрыш составил $', win_sum)
    else:
        win_sum = bet * 10
        print('Победил второй воин, ваш выигрыш составил $', win_sum)
else:
    print('Драка не состоялась, ваша ставка возвращается к вам!')
