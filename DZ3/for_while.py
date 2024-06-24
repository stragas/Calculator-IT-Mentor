# Task 3
numbers = []
total = 0

while True:
  num = int(input("Введите число (или 0 для выхода): "))
  if num == 0:
    break
  numbers.append(num)
  total += num

if numbers:
  average = total / len(numbers)
  print(f"Среднее значение: {average}")
else:
  print("Не было введено ни одного числа.")

 # Task 4

for i in range(101):
    print(i)

 # Task 5

for i in range(10):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()

# Task 6

# Список
my_list = [10, "Hello", True, 3.14, [1, 2, 3]]

print("Список:")
for item in my_list:
  print(item)

# Словарь
my_dict = {"name": "John", "age": 30, "city": "New York"}

print("\nСловарь:")
for key, value in my_dict.items():
  print(f"Ключ: {key}, Значение: {value}")

# Task 7
for i in range(1, 101):
  if i % 3 == 0:
    print(i)

# Task 8
sum = 0
for i in range(1, 101):
  sum += i

print(f"Сумма чисел от 1 до 100: {sum}")

# Task 9

for i in range(1, 11):
  print(f"2 * {i} = {2 * i}")

# Task

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

print("Простые числа от 2 до 50:")
for i in range(2, 51):
  if is_prime(i):
    print(i)

# Task 11
sum_of_squares = 0
for i in range(1, 11):
  sum_of_squares += i**2

print(f"Сумма квадратов чисел от 1 до 10: {sum_of_squares}")

# Task 12

for x in range(1, 11):
    a = x + 0.5
    y = x**2
    b = a**2
    print(f"x = {x}, y = {y}")
    print(f"x = {a}, y = {b}")

# Task 13

for n in range(1, 6):
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  print(f"Факториал {n}: {factorial}")



