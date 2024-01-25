import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os
from dotenv import load_dotenv
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_asyncpg
)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.GET_KEYS['BOT_KEY'])
dp = Dispatcher()

tokens = ['Bitcoin', 'Ethereum', 'Tether USDt', 'BNB', 'Solana', 'XRP', 'USDC', 'Cardano', 'Dogecoin', 'Avalanche', 'TRON', 'Chainlink', 'Polkadot', 'Toncoin', 'Polygon', 'Dai', 'Shiba Inu', 'Litecoin', 'Internet Computer', 'Bitcoin Cash']


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        '''
    Hello! 
I am a modern bot for tracking cryptocurrencies. I can:
- tracking the cryptocurrencies
- send you currency data on a schedule

Write /list to select the trackings tokens
    ''')

@dp.message(Command("list"))
async def get_currencies_list(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Bitcoin")],
        [types.KeyboardButton(text="Ethereum")],
        [types.KeyboardButton(text="Tether USDt")],
        [types.KeyboardButton(text="BNB")],
        [types.KeyboardButton(text="Solana")],
        [types.KeyboardButton(text="XRP")],
        [types.KeyboardButton(text="USDC")],
        [types.KeyboardButton(text="Cardano")],
        [types.KeyboardButton(text="Dogecoin")],
        [types.KeyboardButton(text="Avalanche")],
        [types.KeyboardButton(text="TRON")],
        [types.KeyboardButton(text="Chainlink")],
        [types.KeyboardButton(text="Polkadot")],
        [types.KeyboardButton(text="Toncoin")],
        [types.KeyboardButton(text="Polygon")],
        [types.KeyboardButton(text="Dai")],
        [types.KeyboardButton(text="Shiba Inu")],
        [types.KeyboardButton(text="Litecoin")],
        [types.KeyboardButton(text="Internet Computer")],
        [types.KeyboardButton(text="Bitcoin Cash")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer('Please select token to tracking!', reply_markup=keyboard)

    if message.text in tokens:
        await message.answer('Greatly! Next write the time:')
        selected_time = message.text
        # if selected_time:
        #     add_to_db()

        # i 
    
    else:
        await message.answer('Sorry, repeat the token select!')

# @dp.message(Command("select"))
# async def cmd_start(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text="BTC"),
#             types.KeyboardButton(text="USD")
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите способ подачи"
#     )
#     await message.answer("Select tokens", reply_markup=keyboard)


#парсит бд, выбирает юзера, парсит токены и отправляет пользователю
@dp.message(Command("select"))
async def cmd_start(message: types.Message):
    
    Session = sessionmaker(engine)
    session = Session()





# @dp.message(Command("inline_url"))
# async def cmd_inline_url(message: types.Message, bot: Bot):
#     builder = InlineKeyboardBuilder()

#     builder.row(types.InlineKeyboardButton(
#         text="Bitcoin", url="https://github.com")
#     )
#     builder.row(types.InlineKeyboardButton(
#         text="Ethereum",
#         url="tg://resolve?domain=telegram")
#     )

#     # user_id =message.from_user.id
#     # chat_info = await bot.get_chat(user_id)

#     await message.answer(
#         'Выберите ссылку',
#         reply_markup=builder.as_markup(),
#     )
# сделать:
# 1. пользователь выбирает валюты
# 2. подтверждает выбор
# 3. данные идут в бд как ['user_name', 'user_id', 'requests', 'request_time']
# 4. бот пробегается по базе данных и парсит данные, и отправляет значение валюты пользователю по расписанию

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())