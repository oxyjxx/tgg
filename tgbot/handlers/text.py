from aiogram import types, Dispatcher
from main_bot import dp
from tgbot.keyboards import btn

async def text_checker(message: types.Message):
	if message.text == "/start" and "/help":
		pass
	if message.text == "Ссылки📌":
		await message.reply("Используйте кнопки под сообщением для перехода🔍💗", reply_markup=btn)
		return
	if message.text == "Партнёры🔍":
		await message.reply("К сожалению, партнёров у нас нету :(")
		return
	else:
		pass

def register_handlers_text(dp: Dispatcher):
	dp.register_message_handler(text_checker)