import random

class InvalidRangeError(Exception):
    pass

def generate_random_number(lower, upper):
    try:
        if lower >= upper:
            raise InvalidRangeError("Invalid range. Lower bound must be less than upper bound.")
        number = random.randint(lower, upper)
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Random number {number} generated successfully in range [{lower}, {upper}].\n")
        return number
    except InvalidRangeError as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Failed to generate random number: {str(e)}\n")
        print(f"Error: {str(e)}")

# Пример использования:
while True:
    try:
        lower_bound = int(input("Введите нижнюю границу диапазона: "))
        upper_bound = int(input("Введите верхнюю границу диапазона: "))
        random_number = generate_random_number(lower_bound, upper_bound)
        if random_number is not None:
            print(f"Случайное число в диапазоне [{lower_bound}, {upper_bound}]: {random_number}")
            break
    except ValueError:
        print("Ошибка: Введите целочисленные значения для границ диапазона.")
