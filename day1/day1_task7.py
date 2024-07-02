# Напишите программу, которая принимает на вход температуру в градусах Цельсия 
# и переводит ее в градусы Фаренгейта или наоборот, в зависимости от выбора пользователя.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Добро пожаловать в конвертер температур!\nВыберите режим:")
    print("1. Перевести из Цельсия в Фаренгейт")
    print("2. Перевести из Фаренгейта в Цельсий")
    
    choice = input("Введите 1 или 2: ")
    
    if choice == '1':
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} градусов Цельсия равно {fahrenheit:.2f} градусам Фаренгейта.")
    elif choice == '2':
        fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} градусов Фаренгейта равно {celsius:.2f} градусам Цельсия.")
    else:
        print("Некорректный выбор. Пожалуйста, перезапустите программу и выберите 1 или 2.")

if __name__ == "__main__":
    main()