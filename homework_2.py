class Person:
    def __init__(self,name,age,profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} лет, я {self.profession}')

class Classmate(Person):
    def __init__(self,name,age,profession,group_name):
        super().__init__(name, age, profession)
        self.group_name = group_name

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я одногруппник из группы {self.group_name}. Я {self.profession}')


class Friend(Person):
    def __init__(self,name,age,profession,hobby):
        super().__init__(name,age,profession)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я друг. Моё хобби {self.hobby}. Я {self.profession}')

classmate = Classmate('Мухамедали', 18, 'студент', 71.1)
classmate2 = Classmate('Акмарал', 18, 'студент', 71.1)

friend = Friend('Айдина', 18, 'студент', 'смотреть сериалы')

classmate.introduce()
classmate2.introduce()
friend.introduce()



