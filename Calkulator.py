def main(input: str) -> str:

    elements = input.split()
    if len(elements) != 3:
        raise Exception("Неподдерживаемый формат ввода")


    operand1 = elements[0]
    operand2 = elements[2]
    if operand1.isdigit() and operand2.isdigit():
        operand1 = int(operand1)
        operand2 = int(operand2)
    else:
        raise Exception("Операнды должны быть целыми числами от 1 до 10")
    if not (1 <= operand1 <= 10) or not (1 <= operand2 <= 10):
        raise Exception("Операнды должны быть целыми числами от 1 до 10")


    operator = elements[1]
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 // operand2
    else:
        raise Exception("Проверьте формат ввода: возможные операции: +, -, *, /")

    return str(result)



input_str = input("Введите выражение для вычисления(в формате - число операция число): ")
print(main(input_str))
