import math

class NegativeDiscriminantError(Exception):
    pass

def solve_quadratic_equation(a, b, c):
    try:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise NegativeDiscriminantError("Negative discriminant. Please try again with different coefficients.")
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            with open('log.txt', 'a') as log_file:
                log_file.write(f"Equation {a}x^2 + {b}x + {c} solved successfully. Roots: {x1}, {x2}\n")
            return x1, x2
    except NegativeDiscriminantError as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Equation {a}x^2 + {b}x + {c} failed: {str(e)}\n")
        print(f"Error: {str(e)}")

# Пример использования:
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = solve_quadratic_equation(a, b, c)
if roots:
    print(f"Корни уравнения {a}x^2 + {b}x + {c} равны: {roots}")
