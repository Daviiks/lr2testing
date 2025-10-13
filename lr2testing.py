import random
import decimal

class RandomNumberGenerator:
    """Класс для генерации случайных вещественных чисел в заданном диапазоне"""
    
    def __init__(self):
        self.last_error = None
    
    def validate_input(self, a_str, b_str, n_str):
        """
        Валидация входных данных
        
        Args:
            a_str (str): нижняя граница диапазона
            b_str (str): верхняя граница диапазона  
            n_str (str): количество знаков после запятой
            
        Returns:
            tuple: (bool, str) - успешность валидации и сообщение об ошибке
        """
        self.last_error = None
        
        # Проверка на заполненность всех полей
        if not a_str or not b_str or not n_str:
            self.last_error = "Все поля должны быть заполнены"
            return False, self.last_error
        
        try:
            a = float(a_str)
            b = float(b_str)
            n = int(n_str)
        except ValueError:
            self.last_error = "Некорректный формат чисел"
            return False, self.last_error
        
        # Проверка условия a ≤ b
        if a > b:
            self.last_error = "Нижняя граница (a) должна быть меньше или равна верхней (b)"
            return False, self.last_error
        
        # Проверка количества знаков после запятой
        if n < 0 or n > 15:
            self.last_error = "Количество знаков после запятой должно быть от 0 до 15"
            return False, self.last_error
        
        return True, "Валидация успешна"
    
    def generate_random_number(self, a_str, b_str, n_str):
        """
        Генерация случайного вещественного числа
        
        Args:
            a_str (str): нижняя граница диапазона
            b_str (str): верхняя граница диапазона
            n_str (str): количество знаков после запятой
            
        Returns:
            tuple: (bool, str/float) - успешность операции и результат/ошибка
        """
        is_valid, error_msg = self.validate_input(a_str, b_str, n_str)
        
        if not is_valid:
            return False, error_msg
        
        try:
            a = float(a_str)
            b = float(b_str)
            n = int(n_str)
            
            # Генерация случайного числа
            random_number = random.uniform(a, b)
            
            # Округление до n знаков после запятой
            result = round(random_number, n)
            
            # Для целых чисел убираем .0
            if n == 0:
                result = int(result)
            
            return True, result
            
        except Exception as e:
            self.last_error = f"Ошибка при генерации: {str(e)}"
            return False, self.last_error
    
    def get_last_error(self):
        """Получить последнюю ошибку"""
        return self.last_error
