# If Else

# Задача 1: Количество положительных чисел
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

positive_count = 0
if first_number > 0:
  positive_count += 1
if second_number > 0:
  positive_count += 1
if third_number > 0:
  positive_count += 1

print(f"Количество положительных чисел: {positive_count}")

# Задача 2: Большее из двух чисел
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

if first_number > second_number:
  print(f"Больше число: {first_number}")
else:
  print(f"Больше число: {second_number}")

# Задача 3: Вывод большего и меньшего чисел
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

if first_number > second_number:
  print(f"Больше число: {first_number}, Меньше число: {second_number}")
else:
  print(f"Больше число: {second_number}, Меньше число: {first_number}")

# Задача 4: Наименьшее из трех чисел
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

min_number = first_number
if second_number < min_number:
  min_number = second_number
if third_number < min_number:
  min_number = third_number

print(f"Наименьшее число: {min_number}")

# Задача 5: Координатная четверть
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

if x > 0 and y > 0:
  print("Точка находится в первой четверти")
elif x < 0 and y > 0:
  print("Точка находится во второй четверти")
elif x < 0 and y < 0:
  print("Точка находится в третьей четверти")
else:
  print("Точка находится в четвертой четверти")

# Switch Case

# Задача 1: Оценка по числу
k = int(input("Введите оценку (1-5): "))

match k:
  case 1:
    print("плохо")
  case 2:
    print("неудовлетворительно")
  case 3:
    print("удовлетворительно")
  case 4:
    print("хорошо")
  case 5:
    print("отлично")
  case _:
    print("ошибка")

# Задача 2: Количество дней в месяце
month = int(input("Введите номер месяца (1-12): "))

match month:
  case 1 | 3 | 5 | 7 | 8 | 10 | 12:
    print("31 день")
  case 4 | 6 | 9 | 11:
    print("30 дней")
  case 2:
    print("28 дней")


# Задача 3: Следующая дата
d = int(input("Введите день: "))
m = int(input("Введите месяц: "))

match m:
  case 1 | 3 | 5 | 7 | 8 | 10 | 12:
    if d == 31:
      d = 1
      m += 1
    else:
      d += 1
  case 4 | 6 | 9 | 11:
    if d == 30:
      d = 1
      m += 1
    else:
      d += 1
  case 2:
    if d == 28:
      d = 1
      m += 1
    else:
      d += 1

print(f"Следующая дата: {d}.{m}")

# Задача 4: Направление робота
c = input("Введите исходное направление робота (С, З, Ю, В): ")
n = int(input("Введите команду (0, 1, -1): "))

match c:
  case "С":
    if n == 1:
      c = "З"
    elif n == -1:
      c = "В"
  case "З":
    if n == 1:
      c = "Ю"
    elif n == -1:
      c = "С"
  case "Ю":
    if n == 1:
      c = "В"
    elif n == -1:
      c = "З"
  case "В":
    if n == 1:
      c = "С"
    elif n == -1:
      c = "Ю"

print(f"Направление робота: {c}")

# Задача 5: Описание числа

number = int(input("Введите число (100-999): "))

hundreds = number // 100
tens = (number % 100) // 10
units = number % 10

description = ""

if hundreds == 1:
  description = "сто"
elif hundreds > 1:
  match hundreds:
    case 2:
      description = "двести"
    case 3:
      description = "триста"
    case 4:
      description = "четыреста"
    case 5:
      description = "пятьсот"
    case 6:
      description = "шестьсот"
    case 7:
      description = "семьсот"
    case 8:
      description = "восемьсот"
    case 9:
      description = "девятьсот"

if tens == 1:
  match units:
    case 0:
      description += " десять"
    case 1:
      description += " одиннадцать"
    case 2:
      description += " двенадцать"
    case 3:
      description += " тринадцать"
    case 4:
      description += " четырнадцать"
    case 5:
      description += " пятнадцать"
    case 6:
      description += " шестнадцать"
    case 7:
      description += " семнадцать"
    case 8:
      description += " восемнадцать"
    case 9:
      description += " девятнадцать"
else:
  if tens > 1:
    match tens:
      case 2:
        description += " двадцать"
      case 3:
        description += " тридцать"
      case 4:
        description += " сорок"
      case 5:
        description += " пятьдесят"
      case 6:
        description += " шестьдесят"
      case 7:
        description += " семьдесят"
      case 8:
        description += " восемьдесят"
      case 9:
        description += " девяносто"

  if units > 0:
    match units:
      case 1:
        description += " один"
      case 2:
        description += " два"
      case 3:
        description += " три"
      case 4:
        description += " четыре"
      case 5:
        description += " пять"
      case 6:
        description += " шесть"
      case 7:
        description += " семь"
      case 8:
        description += " восемь"
      case 9:
        description += " девять"

print(f"{number}: {description}")


# Задача: Калькулятор

first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
  result = first_number + second_number
elif operation == "-":
  result = first_number - second_number
elif operation == "*":
  result = first_number * second_number
elif operation == "/":
  if second_number == 0:
    result = "Деление на ноль"
  else:
    result = first_number / second_number
else:
  result = "Неверная операция"

print(f"Результат: {result}")
