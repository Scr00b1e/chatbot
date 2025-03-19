
import logging
import asyncio
from aiogram import Bot, Dispatcher

from config import TG_TOKEN
from app.handlers import router

bot = Bot(TG_TOKEN)
dp = Dispatcher()

async def main():
    await bot.delete_webhook()

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')