# Создайте программу, которая генерирует случайное число 
# в определенном диапазоне и выводит его на экран.
import random

def main():
    lower_bound = int(input("Введите нижнюю границу диапазона: "))
    upper_bound = int(input("Введите верхнюю границу диапазона: "))
    
    if lower_bound > upper_bound:
        print("Некорректный диапазон. Нижняя граница должна быть меньше или равна верхней границе.")
        return
    
    random_number = random.randint(lower_bound, upper_bound)
    
    print(f"Случайное число: {random_number}")

if __name__ == "__main__":
    main()