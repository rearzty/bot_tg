import telebot
import random
from telebot.types import ReactionTypeEmoji
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)

# Запуск бота
bot.polling()
