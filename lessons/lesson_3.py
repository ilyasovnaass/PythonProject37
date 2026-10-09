"""Инкапсуляция"""
# Инкапсуляция -- это защита данных, т.е это когда мы прячем внутренние данные объекта и даем доступ к ним только через
# специальные методы
# для этого часто используют __ , но это не абсолютная защита данных, а механизм ограничения доступа
# class Bank:
#     def __init__(self,login,password,balance):
#         self.login = login
#         self.__password = password    # тут мы сделали приватным пароль через __ (доступно только в 1 классе)
#         self._balance = balance    # тут мы скрыли внутреннюю сумму баланса _ (защищенные, также их можно исп-ть в дочернем классе)
#
#     def get_balance(self, user_login, user_password):
#         if self.login == user_login and self.__password == user_password:
#             return self._balance
#         return 'Не верный логин или же пароль!'
#
#     def __reset_pass(self):     # это приватный метод созданный с помощью __
#         return f'{self.login} Пароль сброшен! Новый пароль 1234!!'
#
#     def new_password(self, old_password):
#         if old_password == self.__password:
#             return self.__reset_pass()
#         return 'Неверный старый пароль!!'
#
#
# account = Bank('akmaral1202',1120,5000)
# print(account.get_balance('akmaral1202',1120))

"""Абстракция"""
# абстракция -- это когда мы показываем только то, что человеку нужно для работы с объектом, а ненужные детпли скрываем
# from abc import ABC, abstractmethod
# класс, который наследует от ABC класса, абстрактный класс
# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def voice(self):
#         pass
#
# # Мы говорим что кошка или собака ДОЛЖНЫ двигаться и издавать звук, неважно как они это сделают
# class Dog(Animal):
#     def move(self):
#         print('Step')
#
#     def voice(self):
#         print('Gav')
#
# dog = Dog()
# dog.move()
# dog.voice()

