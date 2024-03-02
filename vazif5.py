# masala1
# 1.	Books (kitoblar) haqida ma'lumotlarni o'zida saqlovchi o'zgarmas ro'yxat (tuple) xosjl qilinglar.
# Shu tupleni ichidagi elementlarni murojaat qilishni osonlashtirish uchun named tuple dan foydalaninglar

# from collections import namedtuple
# Books=namedtuple('Book','book_name book_creator book_year')
#
# book1=('Python dasturlash asoslari','Anvar Narzullayev',2021)
# book2=('Python o`rganamiz ','Matiz Erik',2021),
# book3=(3,'Python o`rganamiz','Lutz Mark',2021),
# book4=(4,'Python o`rganamiz','Mayer K',2021),
#
# kitob=Books(*book1)
#
# print(kitob.book_creator)
# print(kitob.book_year)


# masala2
# 2.	Bot yozing. Bot ichida 3 ta comanda uchun 3 ta handler yozinglar. Botni guruhga ulanglar.
# Bot Potga. yuborilgan matnli habarni guruhga yuborsin.
# Bot bgtga yuborilgan rasmni guruhga yuborsin.
# Bot botoa yuborilgan videoni guruhga yuborsin.
# Bot botga yuborilgan animatsjvani guruhga yuborsin.
# Botni GitHub ga yuklang. GitHubdagi bot linkini uyga vazifa faylini eng tepasiga Ctrl + V.

from telebot import TeleBot
from telebot.types import Message
bot=TeleBot('6895478934:AAGPYudmqSBbcNHmJcuyqz_7fMZ9UvlKvGk')

@bot.message_handler(commands=['start'])

def start_bot(message:Message):
    message_id=message.chat.id
    test_name=message.from_user.full_name
    print(message_id)
    bot.send_message(message_id, f"Assalomu alaukum {test_name}  ")

@bot.message_handler(content_types=["text"])

def message_bot(message: Message):
    message_id=message.chat.id
    bot.copy_message(-4101184442, message_id, message.message_id)

@bot.message_handler(content_types=["photo"])

def message_bot(message: Message):
    message_id=message.chat.id
    bot.copy_message(-4101184442, message_id, message.message_id)

@bot.message_handler(content_types=["animation"])
def animatsiya(message:Message):
    animatsiya_id=message.chat.id
    bot.copy_message(-4101184442,animatsiya_id,message.message_id)

bot.polling()



















