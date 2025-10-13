import tkinter as tk
from tkinter import ttk, messagebox
from lr2testing import *

class RandomNumberGeneratorGUI:
    """Графический интерфейс для генератора случайных чисел"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных вещественных чисел")
        self.root.geometry("640x480")
        self.root.resizable(True, True)
        
        # Инициализация логического ядра
        self.generator = RandomNumberGenerator()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Заголовок
        title_label = ttk.Label(main_frame, text="Генератор случайных вещественных чисел", 
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Поле для нижней границы (a)
        ttk.Label(main_frame, text="Нижняя граница (a):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_a = ttk.Entry(main_frame, width=20)
        self.entry_a.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Поле для верхней границы (b)
        ttk.Label(main_frame, text="Верхняя граница (b):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_b = ttk.Entry(main_frame, width=20)
        self.entry_b.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Поле для количества знаков после запятой
        ttk.Label(main_frame, text="Знаков после запятой (n):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_n = ttk.Entry(main_frame, width=20)
        self.entry_n.insert(0, "2")  # Значение по умолчанию
        self.entry_n.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Кнопка генерации
        self.generate_btn = ttk.Button(main_frame, text="Сгенерировать", command=self.generate_number)
        self.generate_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Поле для вывода результата
        ttk.Label(main_frame, text="Результат:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(main_frame, textvariable=self.result_var, 
                                     state="readonly", width=20, font=("Arial", 10))
        self.result_entry.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Кнопка копирования
        self.copy_btn = ttk.Button(main_frame, text="Скопировать", command=self.copy_to_clipboard)
        self.copy_btn.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Настройка весов для растягивания
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def generate_number(self):
        """Обработчик нажатия кнопки генерации"""
        a = self.entry_a.get().strip()
        b = self.entry_b.get().strip()
        n = self.entry_n.get().strip()
        
        success, result = self.generator.generate_random_number(a, b, n)
        
        if success:
            self.result_var.set(str(result))
            self.status_var.set("Число успешно сгенерировано")
        else:
            self.result_var.set("")
            messagebox.showerror("Ошибка", result)
            self.status_var.set("Ошибка: " + result)
    
    def copy_to_clipboard(self):
        """Копирование результата в буфер обмена"""
        result = self.result_var.get()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.status_var.set("Результат скопирован в буфер обмена")
        else:
            self.status_var.set("Нет данных для копирования")

def main():
    """Запуск приложения"""
    root = tk.Tk()
    app = RandomNumberGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
