# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def convert_seconds(seconds):
    days = seconds // 86400
    seconds %= 86400
    
    hours = seconds // 3600
    seconds %= 3600
    
    minutes = seconds // 60
    seconds %= 60
    
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

try:
    total_seconds = int(input("Введите количество секунд: "))
    if total_seconds < 0:
        raise ValueError("Количество секунд не может быть отрицательным.")
    result = convert_seconds(total_seconds)
    print(result)
except ValueError as e:
    print(f"Ошибка ввода: {e}")
