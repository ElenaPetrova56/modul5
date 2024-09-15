class House:
    # Атрибут класса для подсчета созданных объектов
    count = 0

    def __new__(cls, *args, **kwargs):
        # Создаем новый экземпляр
        instance = super(House, cls).__new__(cls)
        # Увеличиваем счетчик созданных экземпляров
        cls.count += 1
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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

# Создание экземпляров класса House
house1 = House("Дом 1", 3)
house2 = House("Дом 2", 4)

# Проверяем общее количество созданных объектов
print(f"Всего создано домов: {House.count}")

# Сравниваем дома
print(house1 == house2)
print(house1 < house2)


print(house1)
print(house2)





