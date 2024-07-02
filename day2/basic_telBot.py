import telebot

API_TOKEN = '7021618115:AAE6ZLhNvn2UcBPe41itRf2YeiuL6Kdo8fE'

bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я ваш бот. Чем могу помочь?")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Вот список доступных команд:\n"
        "/start - Начать работу с ботом\n"
        "/help - Получить список доступных команд\n"
        "/perevorot - Перевернуть текст в вашем сообщении\n"
        "/caps - Преобразовать текст в заглавные буквы\n"
        "/cut - Будет удалять все гласные буквы"
    )
    bot.send_message(message.chat.id, help_text)

def extract_text_after_command(message, command):
    # Извлекает текст после команды из сообщения.
    return message.text[len(command):].strip()

# Обработчик команды /perevorot
@bot.message_handler(commands=['perevorot'])
def perevorot(message):
    text_to_reverse = extract_text_after_command(message, '/perevorot')
    if text_to_reverse:
        reversed_text = text_to_reverse[::-1]
        bot.send_message(message.chat.id, reversed_text)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введите текст после команды /perevorot.")

# Обработчик команды /caps
@bot.message_handler(commands=['caps'])
def caps(message):
    text_to_convert = extract_text_after_command(message, '/caps')
    if text_to_convert:
        uppercase_text = text_to_convert.upper()
        bot.send_message(message.chat.id, uppercase_text)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введите текст после команды /caps.")

# Обработчик команды /cut
@bot.message_handler(commands=['cut'])
def cut(message):
    text_to_cut = extract_text_after_command(message, '/cut')
    if text_to_cut:
        vowels = "AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя"
        cut_text = ''.join([char for char in text_to_cut if char not in vowels])
        bot.send_message(message.chat.id, cut_text)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введите текст после команды /cut.")

# Дополнительный обработчик для текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю эту команду. Попробуйте /help для списка команд.")

# Запуск бота
if __name__ == '__main__':
    print("Bot is polling...")
    bot.polling(none_stop=True)