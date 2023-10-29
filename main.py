#from randomizer import random_bool
#random_bool()

import random


#cost = 1
variant = (True, False)
choice = random.choice(variant)
peoplelist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
choicepeople = random.choice(peoplelist)
cost = int(1)
ost = int(1)
kassa = (cost * choicepeople)
print('Водитель бодр и готов к выезду!')
print('Водитель, выбери маршрут! \n 1 \n или \n 2')
route = int(input())
while choice == True:

    if route == 1:
        ost += 9
        cost += 11
        print('Выбран маршрут', route, ', поехали!')
        print('Количество остановок:', ost)
        pass
    if route == 2:
        ost += 19
        cost += 12
        print('Выбран маршрут', route, ', поехали!')
        print('Количество остановок:', ost)
        pass
    if route >= 3:
        print('Последняя попытка! Еще раз подумай, и выбери корректное значение \n 1 \n или \n 2:')
        route = int(input())
        if route >= 3:
            print('Возникла ошибка: введено некорректное значение', route)
            pass


    print('drive in progress')

    if choice == True:
        zaeb = (str('не заебались'))
        pass
    if choice == False:
        zaeb = (str('заебались'))
    print('Вы работали на маршруте', route, ', и перевезли', choicepeople, ' пассажиров, в кассе', kassa, 'рублей.')
    print('Вы заебались, дальнейшая работа невозможна!')
    break


else:
    print('Вы работали на маршруте', route, ', и перевезли', choicepeople, ' пассажиров, в кассе', kassa, 'рублей.')
    print('Вы заебались, дальнейшая работа невозможна!')
