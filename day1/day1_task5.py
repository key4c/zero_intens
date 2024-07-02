# Напишите программу, которая принимает на вход целое число и определяет, 
# является ли оно четным или нечетным.

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Число четное."
    else:
        return "Число нечетное."

try:
    number = int(input("Введите целое число: "))
    result = is_even_or_odd(number)
    print(result)
except ValueError:
    print("Ошибка ввода: Пожалуйста, введите целое число.")