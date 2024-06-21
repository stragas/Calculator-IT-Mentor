import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def solve_quadratic(a, b, c):
    """Решает квадратное уравнение ax^2 + bx + c = 0."""

    # Вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    try:
        if discriminant < 0:
            raise ValueError("Дискриминант отрицателен")

        # Извлекаем корни уравнения
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        return root1, root2

    except ValueError as e:
        logger.error(e)
        raise e

    finally:
        logger.info("Операция завершена")


# Пример использования функции
try:
    a, b, c = map(float, input("Введите коэффициенты a, b и c: ").split())
    roots = solve_quadratic(a, b, c)
    print(f"Корни уравнения: {roots}")
except ValueError as e:
    print(f"Произошла ошибка: {e}")
