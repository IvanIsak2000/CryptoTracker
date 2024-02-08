import logging
from config import settings
import asyncio
from aiogram import Bot, Dispatcher

from handlers import new_order 
from handlers import orders_handler


async def main():
    bot = Bot(token=settings.GET_KEYS['BOT_KEY'])
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)


    dp.include_routers(
        new_order.router,
        orders_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())