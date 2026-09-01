MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0


#Task1
def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Рассчитывает стоимость партии дисков с учётом жанровой скидки.

    Args:
        quantity (int): Количество дисков в партии.
        rental_rate (float): Стоимость аренды одного диска.
        discount (float, optional): Скидка в долях (0.0 = 0%, 0.1 = 10%).
            По умолчанию 0.0.

    Returns:
        tuple[float, bool]: Кортеж из двух элементов:
            - final_sum (float): Итоговая сумма, округлённая до 2 знаков.
            - is_limit_exceeded (bool): True, если сумма превышает лимит.
    """
    final_sum = quantity * rental_rate * (1 - discount)
    final_sum = round(final_sum, 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return (final_sum, is_limit_exceeded)

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

result_1 = calculate_rental_batch(30, 2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма {result_1[0]}$. Превышение лимита: {result_1[1]}")

result_2 = calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.1)
print(f"Партия 2 (Affair Prejudice): Сумма {result_2[0]}$. Превышение лимита: {result_2[1]}")

result_3 = calculate_rental_batch(10, 1.99)
print(f"Партия 3 (Agent Truman): Сумма {result_3[0]}$. Превышение лимита: {result_3[1]}")

result_4 = calculate_rental_batch(quantity=50, rental_rate=3.50, discount=0.2)
print(f"Партия 4 (African Egg): Сумма {result_4[0]}$. Превышение лимита: {result_4[1]}")


#Task2
import time
from typing import Callable, Any

def performance_logger(func: Callable) -> Callable:
    """
    Декоратор для замера времени выполнения функции.

    Принимает целевую функцию, замеряет время её работы через
    time.perf_counter() и выводит лог-сообщение.

    Args:
        func (Callable): Целевая функция, которую необходимо обернуть.

    Returns:
        Callable: Обернутая функция (wrapper).
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Внутренняя обёртка, выполняющая замер времени.

        Args:
            *args: Позиционные аргументы целевой функции.
            **kwargs: Именованные аргументы целевой функции.

        Returns:
            Any: Результат работы оригинальной функции.
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        elapsed_rounded = round(elapsed, TIME_DECIMALS)

        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed_rounded} сек.")

        return result

    return wrapper


@performance_logger
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """
    Сортирует список категорий по выручке в порядке убывания.

    Args:
        data (list[dict[str, str | float]]): Список словарей с данными
            по выручке жанров. Каждый словарь содержит ключи
            'category' (str) и 'total_sales' (float).

    Returns:
        list[dict[str, str | float]]: Новый список, отсортированный
            по убыванию значения ключа 'total_sales'.
    """
    return sorted(data, key=lambda item: item["total_sales"], reverse=True)

print("\n=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

print("--- ТЕСТ 1 ---")
test_data1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]
sorted_data1 = get_sorted_report(test_data1)
print("Топ категорий по выручке:")
for i, item in enumerate(sorted_data1, 1):
    print(f"{i}. {item['category']}: {item['total_sales']}")

print("--- ТЕСТ 2 ---")
test_data2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]
sorted_data2 = get_sorted_report(test_data2)
print("Топ категорий по выручке:")
for i, item in enumerate(sorted_data2, 1):
    print(f"{i}. {item['category']}: {item['total_sales']}")

print("--- ТЕСТ 3 ---")
test_data3 = [
    {"category": "Drama", "total_sales": 500.00}
]
sorted_data3 = get_sorted_report(test_data3)
print("Топ категорий по выручке:")
for i, item in enumerate(sorted_data3, 1):
    print(f"{i}. {item['category']}: {item['total_sales']}")


#Task3
def calculate_overdue_fine(days_overdue: Any, fine_rate: float, film_title: str) -> tuple[float, float] | None:
    """
    Безопасно рассчитывает штраф и технический индекс оборачиваемости.

    Обрабатывает ошибки преобразования типов, неверных значений
    и деления на ноль.

    Args:
        days_overdue (Any): Количество дней просрочки в сыром виде
            (строка, число или другой тип).
        fine_rate (float): Ставка штрафа за один день просрочки.
        film_title (str): Название фильма для сообщений об ошибках.

    Returns:
        tuple[float, float] | None: Кортеж (total_fine, return_index)
            при успешном расчёте, или None при возникновении ошибки.
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{film_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return (total_fine, return_index)


    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_title}': {e}")
        return None

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_title}': {e}")
        return None

    except ZeroDivisionError as e:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_title}': {e}")
        return None

    finally:
        print("--- Проверка транзакции возврата завершена ---")

print("\n=== ПРОВЕРКА ВОЗВРАТОВ ===")

calculate_overdue_fine(5, 1.5, "Matrix")
calculate_overdue_fine("пять", 2.0, "Inception")
calculate_overdue_fine(0, 2.5, "Avatar")
calculate_overdue_fine([3], 3.0, "Interstellar")