import config
import editor
import telebot

bot = telebot.TeleBot(config.TOKEN, )
is_second_tm = False

@bot.message_handler(commands=['start'])
def send_question(message):
  global is_second_tm
  is_second_tm = True
  bot.send_message(chat_id=message.chat.id, text='С каким днем поздравляем?')

@bot.message_handler(content_types=['text'])
def send_meme(message):
  global is_second_tm
  if is_second_tm:
    is_second_tm = False
    bot.send_photo(chat_id=message.chat.id, photo=editor.edit_img(message.text))

print('Telegram Bot is working')
bot.infinity_polling()
