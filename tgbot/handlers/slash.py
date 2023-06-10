from aiogram import types, Dispatcher
from main_bot import dp
from tgbot.keyboards import main_keyboard
from tgbot.keyboards import btn
import requests
import json
from main_bot import bot

async def slash_start(message: types.Message):
	await message.reply(f"Приветсвую @{message.from_user.username}👋🏻\n\nЭто бот переходник, для входа в канал\nнажмите на меню\nкнопку « Ссылки📌 ».", reply_markup=main_keyboard)
	return

def fetch(url):
	s = json.loads(requests.get(url).text)
	return s["url"]

async def slash_nsfw(message: types.Message):
	try:
		f = fetch("https://api.waifu.pics/nsfw/waifu")
		g = fetch("https://api.waifu.pics/nsfw/neko")
		h = fetch("https://api.waifu.pics/nsfw/blowjob")
		media = types.MediaGroup()
		media.attach_photo(photo=f)
		media.attach_photo(photo=g)
		media.attach_photo(photo=h)
		await message.answer_media_group(media=media)
		return
	except:
		await message.reply(f"Воу, воу, не так быстро! Попробуйте ещё раз, через пару секунд💞")
		return

def register_handlers_slash(dp: Dispatcher):
	dp.register_message_handler(slash_start, commands=["start"])
	dp.register_message_handler(slash_nsfw, commands=["nsfw"])
