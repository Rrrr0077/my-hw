from telebot import types

def contact_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Отправить номер", request_contact=True)
    kb.add(button1)
    return kb

def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = types.KeyboardButton("Отправить локацию", request_location=True)
    kb.add(button2)
    return kb
