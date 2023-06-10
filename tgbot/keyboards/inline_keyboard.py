from aiogram import types, Dispatcher
from main_bot import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

channel = InlineKeyboardButton(text="Канал", callback_data="channel", url="https://t.me/+kiyX-KeNRC8yZmQy")
chat = InlineKeyboardButton(text="Чатик", callback_data="chat", url="https://t.me/+Kb1s6jGyfj4xNDMy")

btn = InlineKeyboardMarkup(row_width=2).add(channel, chat)

@dp.callback_query_handler(text="channel")
async def channel_callback(callback: types.CallbackQuery):
	await callback.message.reply("Спасибо за вход в наш канал, мы очень этому рады💗")
	await callback.answer()

@dp.callback_query_handler(text="chat")
async def chat_callback(callback: types.CallbackQuery):
	await callback.message.reply("Спасибо за вход в наш чатик, мы очень этому рады💗")
	await callback.answer()