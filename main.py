from aiogram import Bot, Dispatcher
from config import TOKEN
import asyncio






async def main():
  bot = Bot(token=TOKEN)
  dp = Dispatcher(bot=bot)
  await dp.start_polling(bot)

if __name__ == '__main__':
  asyncio.run(main())