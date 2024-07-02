# Интеграция голосовых сообщений в Telegram-бота

import telebot
from gtts import gTTS
import os

# Ваш токен
API_TOKEN = '7499980878:AAE4l06Mrju4vXMkLgDAAOMP7n07oZCAeho'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    user_id = message.from_user.id

    # Синтез речи
    tts = gTTS(text, lang='ru')
    file_path = f"{user_id}.mp3"
    tts.save(file_path)

    # Отправка аудиофайла пользователю
    with open(file_path, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

    # Удаление временного файла
    os.remove(file_path)

# Запуск бота
bot.polling()