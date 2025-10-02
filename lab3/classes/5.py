class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение: {amount}. Баланс теперь: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств! Операция отклонена.")
        else:
            self.balance -= amount
            print(f"Снятие: {amount}. Баланс теперь: {self.balance}")


# ====== Пример работы с вводом ======
owner = input("Введите имя владельца счёта: ")
start_balance = int(input("Введите начальный баланс: "))

acc = Account(owner, start_balance)

print(f"Счёт создан. Владелец: {acc.owner}, Баланс: {acc.balance}")

# Пополнение
dep = int(input("Введите сумму для пополнения: "))
acc.deposit(dep)

# Ещё одно пополнение
dep2 = int(input("Введите ещё сумму для пополнения: "))
acc.deposit(dep2)

# Снятие
wd = int(input("Введите сумму для снятия: "))
acc.withdraw(wd)

# Попытка снять больше, чем есть
wd2 = int(input("Введите сумму для снятия (пробуем больше баланса): "))
acc.withdraw(wd2)
