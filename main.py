# main.py
from gui import DepositApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = DepositApp(root)
    root.mainloop()