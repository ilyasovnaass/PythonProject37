TRIP_COST = 20

class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть больше 0')
        self.__balance += amount

    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            raise ValueError('Недостаточно средств для оплаты поездки')
        self.__balance -= TRIP_COST

card1 = TransportCard("Иван")
card2  = TransportCard("Айсулуу")

card1.add_money(100)
card2.add_money(50)

print(card1.get_owner())
print(card1.get_balance())

card1.pay_for_trip()
print(card1.get_balance())

print(card2.get_owner())
print(card2.get_balance())
card2.pay_for_trip()
card2.pay_for_trip()
print(card1.get_balance())

try:
    card2.pay_for_trip()
except ValueError as error:
    print(error)

try:
    card1.add_money(-50)
except ValueError as error:
    print(error)

try:
    card1.add_money(0)
except ValueError as error:
    print(error)