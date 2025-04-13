# gui.py
import tkinter as tk
from tkinter import messagebox
from deposit import SimpleDeposit, CapitalizedDeposit
from exceptions import InvalidDepositAmount
from decorators import log_execution, check_positive

class DepositApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Подбор вклада")

        # Поля ввода
        tk.Label(root, text="Тип вклада:").grid(row=0, column=0)
        self.deposit_type = tk.StringVar(value="Простой")
        tk.OptionMenu(root, self.deposit_type, "Простой", "Капитализированный").grid(row=0, column=1)

        tk.Label(root, text="Начальная сумма:").grid(row=1, column=0)
        self.principal_entry = tk.Entry(root)
        self.principal_entry.grid(row=1, column=1)

        tk.Label(root, text="Процентная ставка (%):").grid(row=2, column=0)
        self.rate_entry = tk.Entry(root)
        self.rate_entry.grid(row=2, column=1)

        tk.Label(root, text="Срок (в месяцах):").grid(row=3, column=0)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=3, column=1)

        # Кнопка для расчета прибыли
        self.calculate_button = tk.Button(root, text="Рассчитать прибыль", command=self.calculate_profit)
        self.calculate_button.grid(row=4, columnspan=2)

        # Поле для отображения результата
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=5, columnspan=2)

    @log_execution
    @check_positive
    def calculate_profit(self):
        """Метод для расчета прибыли."""
        try:
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            time = float(self.time_entry.get())

            if self.deposit_type.get() == "Простой":
                deposit = SimpleDeposit(principal=principal, rate=rate, time=time)
            else:
                deposit = CapitalizedDeposit(principal=principal, rate=rate, time=time)

            profit = deposit.calculate_profit()
            self.result_label.config(text=f"Прибыль: {profit:.2f} руб.")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
        except InvalidDepositAmount as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = DepositApp(root)
    root.mainloop()