import telebot
from openai import OpenAI
from gtts import gTTS
import os

# Создаем клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I", # дал zerocode
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Токен вашего бота
TELEGRAM_BOT_TOKEN = '7499980878:AAE4l06Mrju4vXMkLgDAAOMP7n07oZCAeho'

# Создаем бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def get_response_from_model(prompt):
    try:
        # Отправляем запрос к модели
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "отвечай в стиле веселый клоун"},
                {"role": "user", "content": prompt}
            ]
        )
        # Извлекаем и возвращаем ответ
        return chat_completion.choices[0].message.content
    except KeyError as e:
        print(f"KeyError: {e}")
        return "Ошибка: неправильный формат ответа от API."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Ошибка: что-то пошло не так при запросе к API."

def text_to_speech(text, lang='ru'):
    tts = gTTS(text=text, lang=lang)
    filename = "response.ogg"
    tts.save(filename)
    return filename

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, и я могу отвечать на твои вопросы с помощью нейросети. Напиши мне что-нибудь!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    response = get_response_from_model(user_input)
    
    # Преобразование текста в голосовое сообщение
    audio_file = text_to_speech(response)
    
    # Отправка голосового сообщения
    with open(audio_file, 'rb') as voice:
        bot.send_voice(message.chat.id, voice)
    
    # Удаление временного аудиофайла
    os.remove(audio_file)

    # Запуск бота
bot.polling()

if __name__ == "__main__":
    print("Бот запущен")