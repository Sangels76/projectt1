import time


class Account:
    def __init__(self):
        self.balance = 1000
        self.history = []
        self.pin = "1234"


class ATM:
    def __init__(self):
        self.account = Account()

    def check_pin(self):
        for i in range(3):
            if input("Введите PIN: ") == self.account.pin:
                return True
            else:
                print(f"Неверный PIN. Осталось попыток: {2 - i}")
        return False

    def work(self):
        print(time.ctime())

        if not self.check_pin():
            print("Доступ заблокирован!")
            return

        while True:
            print("1.Баланс 2.Снять 3.Пополнить 4.История 5.Выход")
            command = input("Выберите: ")

            if command == "1":
                print("Баланс:", self.account.balance)

            elif command == "2":
                amount = float(input("Сумма: "))
                if amount <= self.account.balance:
                    self.account.balance -= amount
                    self.account.history.append("Снятие: " + str(amount))
                    print("Снято:", amount)
                else:
                    print("Недостаточно средств")

            elif command == "3":
                amount = float(input("Сумма: "))
                if amount > 0:
                    self.account.balance += amount
                    self.account.history.append("Пополнение: " + str(amount))
                    print("Пополнено:", amount)
                else:
                    print("Ошибка")

            elif command == "4":
                for op in self.account.history:
                    print(op)

            elif command == "5":
                print("До свидания!")
                break



atm = ATM()
atm.work()
