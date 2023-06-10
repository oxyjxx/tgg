from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

partners = KeyboardButton("Партнёры🔍")
links = KeyboardButton("Ссылки📌")

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

main_keyboard.row(links, partners)