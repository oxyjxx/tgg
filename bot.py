from aiogram.utils import executor
from main_bot import dp

async def on_startup(_):
	print("bot has started...")

#OTHER
from tgbot.handlers import text, slash
#OTHER

slash.register_handlers_slash(dp)
text.register_handlers_text(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)