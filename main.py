import config
import editor
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InlineQueryResultArticle, InputTextMessageContent

bot = telebot.TeleBot(config.TOKEN)
is_second_tm = False

celebration_settings = {
    'font': 'TOYZ',
    'color': 'Anastasia'
}


def settings_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Шрифты', callback_data='font_style'),
               InlineKeyboardButton('Цвета', callback_data='font_color'),
               InlineKeyboardButton('Готово', callback_data='done'))
    return markup


def font_style_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Roboto-Regular', callback_data='Roboto-Regular'),
               InlineKeyboardButton('TOYZ', callback_data='TOYZ'),
               InlineKeyboardButton('<-', callback_data='back'))
    return markup


def font_color_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Colorful', callback_data='Colorful'),
               InlineKeyboardButton('Anastasia', callback_data='Anastasia'),
               InlineKeyboardButton('<-', callback_data='back'))
    return markup


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = InlineQueryResultArticle(
            '1', 'Result1', InputTextMessageContent('hi'))
        r2 = InlineQueryResultArticle(
            '2', 'Result2', InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


@bot.message_handler(commands=['start'])
def send_question(message):
    bot.send_message(
        message.chat.id, 'Это пока не работает, но скоро заработает:')
    bot.send_message(
        message.chat.id, 'Для отображения списков комманд начни вводить: /')
    bot.send_message(
        message.chat.id, 'А вообще')
    bot.send_message(
        message.chat.id, 'Можно ввести /help')
    bot.send_message(
        message.chat.id, 'Он точно работает и покажет, какие команды вообще есть')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '/start - я буду повторять, что у меня что-то не работает')
    bot.send_message(message.chat.id, '/celebrate - по  рыхлому сгенерирую поздравление')
    bot.send_message(message.chat.id, '/settings - настройка шрифта и цвета (пока наполовину не работает, если шо)')


@bot.message_handler(commands=['celebrate'])
def send_question(message):
    global is_second_tm
    is_second_tm = True
    bot.send_message(
        message.chat.id, 'С каким днем поздравляем?')


@bot.message_handler(commands=['settings'])
def open_settings(message):
    bot.send_message(message.chat.id, 'Настрой очки (тут все будет красивенько)',
                     reply_markup=settings_markup())


@bot.message_handler(content_types=['text'])
def send_meme(message):
    global is_second_tm
    if is_second_tm:
        is_second_tm = False
        bot.send_photo(message.chat.id,
                       photo=editor.edit_img(message.text))


# answer_callback_query - уведомления на экран, использую для подтверждения изменния настроек
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global celebration_settings
    if call.data == 'font_style':
        bot.send_message(call.message.chat.id, 'Настройки шрифта (и тут все будет красивенько)',
                         reply_markup=font_style_markup())

    elif call.data == 'Roboto-Regular':
        celebration_settings['font'] = call.data
        bot.answer_callback_query(
            call.id, f'Выбран шрифт {call.data}')

    elif call.data == 'TOYZ':
        celebration_settings['font'] = call.data
        bot.answer_callback_query(
            call.id, f'Выбран шрифт {call.data}')

    elif call.data == 'font_color':
        bot.send_message(call.message.chat.id, 'Настройки цвета (и тут, конечно, все будет красивенько',
                         reply_markup=font_color_markup())

    elif call.data == 'Colorful':
        celebration_settings['color'] = call.data
        bot.answer_callback_query(
            call.id, f'Выбран цвет шрифта {call.data}')

    elif call.data == 'Anastasia':
        celebration_settings['color'] = call.data
        bot.answer_callback_query(
            call.id, f'Выбран цвет шрифта {call.data}')

    elif call.data == 'back':
        bot.send_message(call.message.chat.id, 'Настрой очки (тут все будет красивенько)',
                         reply_markup=settings_markup())

    elif call.data == 'done':
        bot.answer_callback_query(
            call.id, 'Настройки сохранены (на самом деле нет)')
        global is_second_tm
        is_second_tm = True
        bot.send_message(call.message.chat.id,
                         'С каким днем поздравляем?')

    else:
        bot.send_message(call.message.chat.id,
                         'Не, ну, тут ты совсем не прав')


print('Telegram Bot is working')
bot.infinity_polling()
