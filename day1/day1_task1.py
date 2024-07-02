# При заданном целом числе n посчитайте n + nn + nnn.
def calculate_expression(n):
    n1 = n
    n2 = n * 10 + n
    n3 = n * 100 + n * 10 + n
    result = n1 + n2 + n3
    return result

n = int(input("Введите целое число: "))
print(f"Результат n + nn + nnn: {calculate_expression(n)}")