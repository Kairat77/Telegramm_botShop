import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.database.models import async_main
from app.handlers import router
import logging

async def main():
  await async_main()
  bot = Bot(token=TOKEN)
  dp = Dispatcher()
  dp.include_router(router)
  await dp.start_polling(bot)

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Stopped by Ctrl+C")