"""Основы ООП (объектно-ореинтированное программирование). Классы (class)"""
# через классы можно создавать несколько объектов, у которых будут одни и те же функции/свойства
# это удобно тем, что при создании в огромных кол-вах объекты, у которых должны быть одинаковые свойства,
# не надо их вручную переписывать, это занимает много времени и памяти, можно создать 1 класс (типо 1 источник)
# и через этот класс создавать много объектов

# class Cat:  # создаем класс с именем (имя мб разное)
#     name = None     # внутри создаем свойства объекта, который появится позже
#     age = None
#     isHappy = None
#
# cat1 = Cat()    # создали сам объект
# cat1.name = 'Лера'  # приписываем свойства
# cat1.age = 2
# cat1.isHappy = True
# print(cat1.name)    # и выводим результат
# print(cat1.age)
# print(cat1.isHappy)
#
# cat2 = Cat()    # создаем 2й объект и ее свойства
# cat2.name = 'Белка'
# cat2.age = 6
# cat2.isHappy = True
# print(cat2.name)
# print(cat2.age)
# print(cat2.isHappy)
# # можно вот так вот создавать объекты а можно намного укоротить код, создав метод (функция(def))
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_name(self):
#         print("Котенок",self.name,". Возраст",self.age,'. Они счастливы:',self.isHappy)
#
# cat1 = Cat()
# cat1.set_data('Алина', 3,True)
# cat1.get_name()
#
# cat2 = Cat()
# cat2.set_data('Лера',2,True)
# cat2.get_name()

"""Конструкторы"""
# с помощью конструкторов можно сократить код внутри класса
# class Cat:
#     def __init__(self, name, age):  # с помощью __init__ создается сам конструктор
#         self.set_data(name, age)
#         self.get_data()
#     def set_data(self, name = None, age = None ):   # через None можно устанавливать значение по умолчанию, т.е
#         self.name = name                            # не объязательно устанавливать значение в этот параметр,
#         self.age = age
#
#     def get_data(self):
#         print(f'{self.name}: {self.age} годика')
#
# cat1 = Cat('Mimi',3)
# cat2 = Cat('Lili', 2)
#
# cat1.set_data('Lola')   # из-за None теперь можно передавать по желанию 1 или 2 значения в параметр
# cat1.get_data()         # т.е если указано 2 параметра в методе, по умолчанию (через None) можно 1 не передавать

