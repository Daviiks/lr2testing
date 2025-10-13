import unittest
from lr2testing import *

class TestRandomNumberGenerator(unittest.TestCase):
    """Тесты для генератора случайных чисел"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.generator = RandomNumberGenerator()
    
    def test_validation_correct_input(self):
        """Тест корректных входных данных"""
        is_valid, message = self.generator.validate_input("1.5", "10.5", "3")
        self.assertTrue(is_valid)
        self.assertEqual(message, "Валидация успешна")
    
    def test_validation_empty_fields(self):
        """Тест пустых полей"""
        is_valid, message = self.generator.validate_input("", "10", "2")
        self.assertFalse(is_valid)
        self.assertIn("Все поля должны быть заполнены", message)
        
        is_valid, message = self.generator.validate_input("1", "", "2")
        self.assertFalse(is_valid)
        self.assertIn("Все поля должны быть заполнены", message)
        
        is_valid, message = self.generator.validate_input("1", "10", "")
        self.assertFalse(is_valid)
        self.assertIn("Все поля должны быть заполнены", message)
    
    def test_validation_invalid_format(self):
        """Тест некорректного формата чисел"""
        is_valid, message = self.generator.validate_input("abc", "10", "2")
        self.assertFalse(is_valid)
        self.assertIn("Некорректный формат чисел", message)
        
        is_valid, message = self.generator.validate_input("1", "def", "2")
        self.assertFalse(is_valid)
        self.assertIn("Некорректный формат чисел", message)
        
        is_valid, message = self.generator.validate_input("1", "10", "xyz")
        self.assertFalse(is_valid)
        self.assertIn("Некорректный формат чисел", message)
    
    def test_validation_a_greater_than_b(self):
        """Тест случая когда a > b"""
        is_valid, message = self.generator.validate_input("10", "5", "2")
        self.assertFalse(is_valid)
        self.assertIn("Нижняя граница (a) должна быть меньше или равна верхней (b)", message)
    
    def test_validation_decimal_places_range(self):
        """Тест диапазона количества знаков после запятой"""
        is_valid, message = self.generator.validate_input("1", "10", "-1")
        self.assertFalse(is_valid)
        self.assertIn("Количество знаков после запятой должно быть от 0 до 15", message)
        
        is_valid, message = self.generator.validate_input("1", "10", "16")
        self.assertFalse(is_valid)
        self.assertIn("Количество знаков после запятой должно быть от 0 до 15", message)
    
    def test_generate_number_range(self):
        """Тест на корректность диапазона сгенерированных чисел"""
        # Многократная генерация для проверки диапазона
        a, b, n = 1.0, 10.0, 2
        
        for _ in range(1000):  # Большое количество тестов для надежности
            success, result = self.generator.generate_random_number(str(a), str(b), str(n))
            self.assertTrue(success)
            self.assertIsInstance(result, float)
            self.assertGreaterEqual(result, a)
            self.assertLessEqual(result, b)
    
    def test_generate_number_integer_result(self):
        """Тест генерации целых чисел (n=0)"""
        success, result = self.generator.generate_random_number("1", "10", "0")
        self.assertTrue(success)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)
    
    def test_generate_number_decimal_places(self):
        """Тест количества знаков после запятой"""
        a, b, n = 1.0, 2.0, 3
        
        success, result = self.generator.generate_random_number(str(a), str(b), str(n))
        self.assertTrue(success)
        
        # Проверка количества знаков после запятой
        decimal_places = len(str(result).split('.')[1]) if '.' in str(result) else 0
        self.assertLessEqual(decimal_places, n)
    
    def test_generate_number_edge_cases(self):
        """Тест граничных случаев"""
        # Одинаковые границы
        success, result = self.generator.generate_random_number("5.0", "5.0", "2")
        self.assertTrue(success)
        self.assertEqual(result, 5.0)
        
        # Отрицательные числа
        success, result = self.generator.generate_random_number("-10.5", "-1.5", "1")
        self.assertTrue(success)
        self.assertGreaterEqual(result, -10.5)
        self.assertLessEqual(result, -1.5)
        
        # Большой диапазон
        success, result = self.generator.generate_random_number("0.001", "1000.999", "3")
        self.assertTrue(success)
        self.assertGreaterEqual(result, 0.001)
        self.assertLessEqual(result, 1000.999)
    
    def test_error_handling_in_generate(self):
        """Тест обработки ошибок в методе generate"""
        # Некорректные данные
        success, result = self.generator.generate_random_number("abc", "10", "2")
        self.assertFalse(success)
        self.assertIsInstance(result, str)
        self.assertIn("Некорректный формат чисел", result)
        
        # a > b
        success, result = self.generator.generate_random_number("15", "10", "2")
        self.assertFalse(success)
        self.assertIn("Нижняя граница (a) должна быть меньше или равна верхней (b)", result)

if __name__ == "__main__":
    # Запуск тестов
    unittest.main(verbosity=2)
