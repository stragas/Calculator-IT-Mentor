
#Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

#1.	Дана сторона квадрата a. Найти его периметр P = 4·a
#2.	Дана сторона квадрата a. Найти его площадь{{ S = a2}}
#3.	Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
#4.	Дан диаметр окружности d. Найти ее длину{{ L = π·d, π = 3.14}}
#5.	Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2
#6.	Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)

#7.	Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14
#8.	Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
#9.	Даны два неотрицательных числа a и b. Найти их среднее геометрическое,т.е. квадратный корень из их произведения: (a·b)1/2

#10.	Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

import math

# 1
def square_perimeter(a):
    return 4 * a

# 2
def square_area(a):
    return a**2

# 3
def rectangle_area_and_perimeter(a, b):
    return a * b, 2 * (a + b)

# 4
def circle_length(d):
    return math.pi * d

# 5
def cube_volume_and_surface_area(a):
    return a**3, 6 * a**2

# 6
def rectangular_parallelepiped_volume_and_surface_area(a, b, c):
    return a * b * c, 2 * (a * b + b * c + a * c)

# 7
def circle_length_and_area(R):
    return 2 * math.pi * R, math.pi * R**2

# 8
def arithmetic_mean(a, b):
    return (a + b) / 2

# 9
def geometric_mean(a, b):
    return math.sqrt(a * b)

# 10
def operations_on_squares(a, b):
    sum_squares = a**2 + b**2
    difference_squares = a**2 - b**2
    product_squares = a**2 * b**2
    quotient_squares = a**2 / b**2
    return sum_squares, difference_squares, product_squares, quotient_squares

# Test the functions
a = 5.56
b = 3.87
c = 4.765
d = 8.987
R = 6.98

print(square_perimeter(a))
print(square_area(a))
print(rectangle_area_and_perimeter(a, b))
print(circle_length(d))
print(cube_volume_and_surface_area(a))
print(rectangular_parallelepiped_volume_and_surface_area(a, b, c))
print(circle_length_and_area(R))
print(arithmetic_mean(a, b))
print(geometric_mean(a, b))
print(operations_on_squares(a, b))
