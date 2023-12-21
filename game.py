import random
import string



class Attribute:
    def __init__(self, name: str, hp: int, damage: int, flag: str) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        self.flag = flag



    def kick(self):
       return self.damage

    def loss(self, damage):
        if self.hp > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def team(self):
        return self.flag

warriors = []
flags = ['red', 'blue']
names = []
hit = random.choice([True, False])


for i in range(10000):
    warriors.append(Attribute(name=''.join((random.choice(string.ascii_lowercase) for x in range(10))), hp=100, damage=random.randint(1, 20), flag=random.choice(flags)))

for i in warriors:
    print(i.name, i.flag)


active1 = random.choice(warriors)
active2 = random.choice(warriors)

while (active2.flag != active1.flag) and (active1.hp > 0 or active2.hp <= 0):

    print('Воин', active1.name, 'наносит', active2.damage, 'урона', active2.name, active2.loss(damage=active1.kick()))








# while warrior1.hp > 0 and warrior2.hp > 0:
#     if hit:
#         if warrior1.flag != warrior2.flag:
#             active = random.choice([warrior1, warrior2])
#             if active.name == 'Harald':
#                 print('Воин', warrior1.name, 'наносит', warrior1.damage, 'урона', warrior2.name, warrior2.loss(damage=warrior1.kick()))
#             else:
#                 print('Воин', warrior2.name, 'наносит', warrior2.damage, 'урона', warrior1.name, warrior1.loss(damage=warrior2.kick()))
#
# if warrior1.hp > 0:
#     print('Выиграл', warrior1.name)
# else:
#     print('Выиграл', warrior2.name)











