from openai import OpenAI

# Создаем клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I", # дал zerocode
    base_url="https://api.proxyapi.ru/openai/v1",
)

def get_response_from_model(prompt):
    # Отправляем запрос к модели
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}]
    )
    # Извлекаем и возвращаем ответ
    return chat_completion['choices'][0]['message']['content']

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