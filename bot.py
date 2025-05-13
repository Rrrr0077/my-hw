from telebot import TeleBot
from button import contact_button,location_button
from database import  add_user, update_location
from geopy import Photon



bot = TeleBot("7662884568:AAGFO4MZwyXahTgK3WmmCni0frZ0fyY8_cE")
geolocator = Photon(user_agent="geo-locator", timeout=10)


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    bot.send_message(user_id, f"Привет, {name}! Отправь свой номер телефона.", reply_markup=contact_button())
    bot.register_next_step_handler(message, phone_number, name)

def phone_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone = message.contact.phone_number
        add_user(user_id, name, phone)
        bot.send_message(user_id, f"Спасибо, {name}. Теперь отправь свою локацию.", reply_markup=location_button())
        bot.register_next_step_handler(message, get_location)
    else:
        bot.send_message(user_id, "Пожалуйста, используй кнопку для отправки номера.", reply_markup=contact_button())
        bot.register_next_step_handler(message, phone_number, name)

def get_location(message):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = geolocator.reverse((latitude, longitude)).address
        update_location(user_id, address)
        bot.send_message(user_id, f"Спасибо! Мы сохранили ваш адрес:\n{address}")
    else:
        bot.send_message(user_id, "Пожалуйста, отправьте локацию с помощью кнопки.", reply_markup=location_button())
        bot.register_next_step_handler(message, get_location)

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(message.chat.id, "Нажмите 'Отправить номер', затем — 'Отправить локацию'.")

bot.infinity_polling()
