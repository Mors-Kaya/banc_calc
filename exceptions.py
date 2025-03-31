# exceptions.py
class DepositError(Exception):
    """Базовый класс для исключений, связанных с вкладами."""
    pass


class InvalidDepositAmount(DepositError):
    """Исключение для неверной суммы вклада."""
    def __init__(self, message="Сумма вклада должна быть положительной."):
        self.message = message
        super().__init__(self.message)