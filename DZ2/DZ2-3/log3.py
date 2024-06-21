class InvalidInputError(Exception):
    pass

def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Average of numbers {numbers} calculated successfully: {average}\n")
        return average
    except ZeroDivisionError:
        with open('log.txt', 'a') as log_file:
            log_file.write("Error: Division by zero occurred.\n")
        print("Ошибка: Деление на ноль.")
    except (TypeError, ValueError):
        with open('log.txt', 'a') as log_file:
            log_file.write("Ошибка: Некорректный ввод. Пожалуйста, введите список чисел.\n")
        print("Ошибка: Некорректный ввод. Пожалуйста, введите список чисел.")

# Пример использования:
try:
    user_input = input("Введите список чисел через пробел: ")
    numbers = [float(num) for num in user_input.split()]
    result = calculate_average(numbers)
    if result is not None:
        print(f"Среднее арифметическое чисел {numbers}: {result}")
except Exception as e:
    with open('log.txt', 'a') as log_file:
        log_file.write(f"Произошла ошибка: {str(e)}\n")
