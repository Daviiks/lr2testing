import inspect
from lr2testing import *

def inspect_function(func):
    """
    Функция для интроспекции другой функции
    
    Args:
        func: функция для анализа
    """
    print("=" * 60)
    print("ИНТРОСПЕКЦИЯ ФУНКЦИИ")
    print("=" * 60)
    
    # Имя функции
    print(f"1. Имя функции: {func.__name__}")
    
    # Количество аргументов
    signature = inspect.signature(func)
    parameters = signature.parameters
    print(f"2. Количество аргументов: {len(parameters)}")
    print(f"   Аргументы: {list(parameters.keys())}")
    
    # Является ли встроенной
    is_builtin = inspect.isbuiltin(func)
    print(f"3. Является встроенной: {'Да' if is_builtin else 'Нет'}")
    
    # Исходный код
    print("4. Исходный код:")
    try:
        source_code = inspect.getsource(func)
        print(source_code)
    except (TypeError, OSError) as e:
        print(f"   Не удалось получить исходный код: {e}")
    
    print("=" * 60)


# Демонстрация работы inspect_function
if __name__ == "__main__":
    # Создаем экземпляр класса для тестирования
    generator = RandomNumberGenerator()
    
    print("ДЕМОНСТРАЦИЯ ИНТРОСПЕКЦИИ МЕТОДОВ КЛАССА RandomNumberGenerator")
    print()
    
    # Интроспекция методов класса
    methods_to_inspect = [
        generator.validate_input,
        generator.generate_random_number, 
        generator.get_last_error
    ]
    
    for method in methods_to_inspect:
        inspect_function(method)
        print("\n")
    
    # Также покажем интроспекцию встроенной функции для сравнения
    print("ДЛЯ СРАВНЕНИЯ - ИНТРОСПЕКЦИЯ ВСТРОЕННОЙ ФУНКЦИИ:")
    inspect_function(len)
