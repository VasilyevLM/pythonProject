class Case:
    def __init__ (self, name: str, surname: str, group: int, value: dict):
        self.name = name
        self.surname = surname
        self.group = group
        self.value = value

    def summary(self):
        mid_value = (self.value['математика'] + self.value['информатика']) / 2
        return mid_value



value = {'математика': 5, 'информатика': 4}
value1 = {'математика': 2, 'информатика': 3}
student1 = Case(name='Миша', surname='Иванов', group=123563, value=value)
student2 = Case(name='Илья', surname='Олегов', group=352684, value=value)
student3 = Case(name='Дарья', surname='Кальянова', group=158963, value=value)
student4 = Case(name='Иван', surname='Сергеев', group=123456, value=value)
student5 = Case(name='Ольга', surname='Петрова', group=365896, value=value)
student6 = Case(name='Наталья', surname='Вайсман', group=145962, value=value)
student7 = Case(name='Олег', surname='Кретинов', group=365745, value=value)
student8 = Case(name='Виктор', surname='Сидоров', group=123563, value=value)
student9 = Case(name='Ксения', surname='Гальянова', group=523987, value=value1)
student10 = Case(name='Анатолий', surname='Петров', group=123563, value=value)

students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]
cards = []
for i in students:
    cards.append(i.summary())

cards.sort()
print(cards)












