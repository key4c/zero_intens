# Эхо-бот - это бот, который повторяет то, что мы ему отправляем. 
# Если мы отправим ему сообщение, он просто вернет то же самое сообщение. 
# Это часто используется для тестирования или демонстрации работы ботов.
import telebot

# Вставьте ваш токен здесь
API_TOKEN = '7264959728:AAGBbGKXB_Mhl7NNbvnSULgEzb-vHAq0FoQ'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик для сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Отправляем обратно то же сообщение, которое получили
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    # Запуск бота
    bot.polling(none_stop=True)