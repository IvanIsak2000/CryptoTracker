import logging
import os
from dotenv import load_dotenv
from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from config import settings
import asyncio
from aiogram import Bot, Dispatcher

from handlers import order_currencies_tracker, menu_buttons

async def main():
    bot = Bot(token=settings.GET_KEYS['BOT_KEY'])
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)

    dp.include_routers(
        order_currencies_tracker.router,
        menu_buttons.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    engine = create_engine(
        url=settings.DATABASE_URL_asyncpg
    )

# сделать:
# 1. пользователь выбирает валюты
# 2. подтверждает выбор
# 3. данные идут в бд как ['user_name', 'user_id', 'requests', 'request_time']
# 4. бот пробегается по базе данных и парсит данные, и отправляет значение валюты пользователю по расписанию


if __name__ == "__main__":
    asyncio.run(main())