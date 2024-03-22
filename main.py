import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.database.models import async_main

async def main():
  await async_main()
  bot = Bot(token=TOKEN)
  dp = Dispatcher()
  await dp.start_polling(bot)

if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Stopped by Ctrl+C")