# deposit.py
class Deposit:
    def __init__(self, principal=1000.0, rate=5.0, time=1):
        self._principal = principal  # начальная сумма вклада
        self._rate = rate / 100  # процентная ставка
        self._time = time  # время в годах

    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value

    @property
    def rate(self):
        return self._rate * 100

    @rate.setter
    def rate(self, value):
        self._rate = value / 100

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    def calculate_profit(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def __add__(self, other):
        if isinstance(other, Deposit):
            return Deposit(self.principal + other.principal, self.rate, self.time)

    def __sub__(self, other):
        if isinstance(other, Deposit):
            return Deposit(self.principal - other.principal, self.rate, self.time)


class SimpleDeposit(Deposit):
    def calculate_profit(self):
        return self.principal * self._rate * self.time


class CapitalizedDeposit(Deposit):
    def calculate_profit(self):
        return self.principal * ((1 + self._rate) ** self.time - 1)


class Bank:
    def __init__(self):
        self.deposits = []

    def add_deposit(self, deposit):
        self.deposits.append(deposit)

    def total_profit(self):
        return sum(deposit.calculate_profit() for deposit in self.deposits)