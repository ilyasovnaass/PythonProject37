class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Возраст должен быть положительным!')

    def make_sound(self):
        return 'Животное издает звук'

class Dog(Animal):
    def make_sound(self):
        return 'Гав-гав!'

class Cat(Animal):
    def make_sound(self):
        return 'Мяу!'

dog = Dog('Тузик', 4)
cat = Cat('Муиза', 2)

print(f'{dog.get_name()} говорит: {dog.make_sound()}')
print(f'{cat.get_name()} говорит: {cat.make_sound()}')

cat.set_age(1)
cat.set_name('Kitty')

print(f'После изменения через сеттеры:')
print(f'Имя: {cat.get_name()}, Возраст: {cat.get_age()}')
print(f'Звук: {cat.make_sound()}')
