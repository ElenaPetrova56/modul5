ass House:
    count = 0
    houses_history = []

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.count += 1
        House.houses_history.append(self)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def remove(self):
        House.count -= 1
        House.houses_history.remove(self)

# Использование класса
house1 = House("Дом 1", 3)
house2 = House("Дом 2", 4)

# Проверяем общее количество созданных объектов
print(f"Всего создано домов: {House.count}")

# Сравниваем дома
print(house1 == house2)  # Output: False
print(house1 < house2)   # Output: True

# Печатаем информацию о домах
print(house1)  # Output: Название: Дом 1, кол-во этажей: 3
print(house2)  # Output: Название: Дом 2, кол-во этажей: 4

# Пример удаления дома
house1.remove()

# Проверяем общее количество после удаления
print(f"Всего создано домов после удаления: {House.count}")
