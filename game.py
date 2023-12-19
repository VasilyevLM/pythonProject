import random

# def kick(list_war):
#     active = random.choice(list_war)
#     damage = random.randint(1, 20)
#     hp = active["hp"]
#     hp -= damage
#     active["hp"] = hp
#     if active["name"] == "Первый воин":
#         list_war[0] = active
#     else:
#         list_war[1] = active
#     return list_war
#
#
# list_war = [
#     {"name": "Первый воин", "hp": 100},
#     {"name": "Второй воин", "hp": 100}
# ]
#
#
# while list_war[0]["hp"] > 0 and list_war[1]["hp"] > 0:
#     hit = random.choice([True, False])
#     if hit:
#         list_war = kick(list_war)
#         print(list_war)
#     else:
#         print('не удачно')


class Attribute:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage



    def kick(self):
       return self.damage

    def loss(self, damage):
        if self.hp > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp



warrior1 = Attribute(name='Harald', hp=100, damage=random.randint(1, 20))
warrior2 = Attribute(name='Gustav', hp=100, damage=random.randint(1, 20))


hit = random.choice([True, False])

while warrior1.hp > 0 and warrior2.hp > 0:
    if hit:
        active = random.choice([warrior1, warrior2])
        if active.name == 'Harald':
            print('Воин', warrior1.name, 'наносит', warrior1.damage, 'урона', warrior2.name, warrior2.loss(damage=warrior1.kick()))
        else:
            print('Воин', warrior2.name, 'наносит', warrior2.damage, 'урона', warrior1.name, warrior1.loss(damage=warrior2.kick()))

if warrior1.hp > 0:
    print('Выиграл', warrior1.name)
else:
    print('Выиграл', warrior2.name)











