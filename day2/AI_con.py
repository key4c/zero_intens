from openai import OpenAI

# Создаем клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I", # дал zerocode
    base_url="https://api.proxyapi.ru/openai/v1",
)

def get_response_from_model(prompt):
    try:
        # Отправляем запрос к модели
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": prompt}]
        )
        # Выводим полученный ответ для отладки
        """
        print(chat_completion)
        """  
              
        # Извлекаем и возвращаем ответ
        return chat_completion.choices[0].message.content
    except KeyError as e:
        print(f"KeyError: {e}")
        return "Ошибка: неправильный формат ответа от API."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Ошибка: что-то пошло не так при запросе к API."


def main():
    print("Добро пожаловать в чат с нейросетью! Введите 'exit' для выхода.")
    while True:
        # Получаем ввод пользователя
        user_input = input("Вы: ")
        if user_input.lower() == 'exit':
            print("Выход из чата...")
            break
        
        # Получаем ответ от модели
        response = get_response_from_model(user_input)
        print(f"Нейросеть: {response}")

if __name__ == "__main__":
    main()