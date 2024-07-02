# Создайте простой калькулятор, который позволяет пользователю 
# вводить два числа и выполнять над ними основные арифметические 
# операции (сложение, вычитание, умножение, деление).
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def calculator():
    print("Выберите операцию: 1 - '+', 2 - '-', 3 - '*', 4 - '/' ")


    try:
        choice = input("Введите номер операции: ")
        if choice not in ['1', '2', '3', '4']:
            raise ValueError("Недопустимая операция")

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    calculator()