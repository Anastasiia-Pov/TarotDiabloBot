from aiogram import Bot, Dispatcher
import logging
import asyncio
from config import token
from app.handlers import router
# from database.models import async_main


async def main():
    # await async_main()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
