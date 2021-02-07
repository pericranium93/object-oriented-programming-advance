# class Car:
#     def __init__(self):
#         self.modules = []
#         self.fc = 7
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self  # возвращаем сам объект. нужно для car + 1 + 2 + 3
#
#     def __str__(self):
#         return f'{self.modules}'
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         # self.__dict__[key] = value  # второй способ добавление аттрибута в системный словарьб
#         print(f'Создан ключ {key} со значением {value}')  # можно применять для вывода информации в консоль, записи в файл (логирование)
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     # def __call__(self, *args, **kwargs):
#     def __call__(self, price=None):
#         return f'ваша машина с модулями {self.modules} стоит {price}'
#
#
#     def __del__(self):  # деструктор, удаляет весь мусор (допустим, не используемые более объекты) можно так же использовать для логирования или сохранения данных запускается автоматом
#         print('объект удален')
#
#     def __eq__(self, other):
#         return self.fc == other


# car = Car()
# module_1 = 'тёплый руль'
# module_2 = 'ракеты'
# module_3 = 'камеры'
# del car  # можно принудительно удалять объекты, но используется редко

# car.modules.append(module_1)
# car.modules.append(module_2)
# car.modules.append(module_3)
# print(car.modules)

# car + module_1  # при заданном методе __add__ работает как append
# car + module_2  # car.__add__(module_2)
# car + module_3

# a = 1 + 1  # c = 1; a = c.__add__(1)  == 2
#
# car + module_1 + module_2 + module_3  # для того, чтобы работало необходимо в методе вернуть сам объект
# car.wheel = 'Tesla'  # обращается к системному методу __setattr__
# print(car.modules)
# print(car)  # print запускает модуль __str__, модифицировав его можем укоротить вывод print(car.modules)
# print(car[0])  # обращается к системному методу __getitem__, но car у нас стринговый
#
# print(car(price=5000))  # обращается к системному методу __call__
# print(car())  # обращается к системному методу __call__
#
# print(car == 7)  # # обращается к системному методу __eq__
# print(car == 8)


#############Интерфей итерации################### работает с for, map, filter, zip и распаковка (*qwe)
# my_list = [10, 20, 30, 40]  # приверяет на наличие итер-объекта __iter__
# for i in my_list:  # __iter__ => object => __next__ => __next__ => ... => StopIteration (исключение)
#     print(i)

# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):  # возвращаем итерируемый объект
#         return self
#
#     def __next__(self):  # указывает внутри итерируемого класса
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# qwe = Iterator()
# # for i in qwe:
# #     print(i)
# print(*qwe)


########### Интерфейс абстрактного класса ##############

# from abc import ABC, abstractmethod
#
#
# class MyAbsClass(ABC):  # шаблон, который может содерджать какой-то обязательный функционал или структуру. от него наследуется класс и в дальнейшем перегружается и модифицируется
#     @abstractmethod
#     def __init__(self):
#         pass
#     @abstractmethod  # оборачивает функцию в декоратор абстракт-метод
#     def my_method_1(self):
#         pass
#
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
#
# class MyClass(MyAbsClass):
#     def my_method_1(self):
#         print('qwe')
#
#     def my_method2(self):  # должен выдавать ошибку, если метод назван не верно
#         print('rhg')
#
#
# z = MyClass()


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property  # избавляет от необходимости изменять код (дописывать везде (), так как age стал методом, а не атрибутом) теперь код можно оставить таким же, т.к. метод age будет выглядеть как атрибут
#     def age(self):
#         # if self._age < 0 .....  # проверки
#         return self._age
#
#
# # much code
# human = Human('Ivan', 50)
# print(human.age)


######### Композиция (Класс-контейнер) #############

# class WinDor:
#     def __init__(self, wd_l, wd_h):
#         self.square = wd_l * wd_h
#
# class Room:
#     def __init__(self, l1, l2, h):
#         self.square = 2 * h * (l1 + l2)
#         self.wd = []
#
#     def add__windor(self, wd_l, wd_h):
#         self.wd.append(WinDor(wd_l, wd_h))  # композиция используем внутри класса другой класс
#
#     def common_square(self):
#         main_square = self.square
#         for el in self.wd:
#             main_square -= el.square
#         return main_square
#
#
# r = Room(7, 4, 3)
# print(r.square)
# r.add__windor(2, 2)
# r.add__windor(2, 3)
# r.add__windor(1, 1)
# r.add__windor(2, 1)
# print(r.common_square())
