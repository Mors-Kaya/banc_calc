import time
from functools import wraps

def log_execution(func):
    """Декоратор для логирования выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнена за {end_time - start_time:.4f} секунд.")
        return result
    return wrapper

def check_positive(func):
    """Декоратор для проверки положительных значений."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            # Проверяем, является ли аргумент числом
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Аргументы должны быть положительными.")
        return func(*args, **kwargs)
    return wrapper