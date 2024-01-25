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
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# from keyboards.simple_row import make_row_keyboard

from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_asyncpg
)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.GET_KEYS['BOT_KEY'])
dp = Dispatcher()

# router = Router()

currencies = ['Bitcoin', 'Ethereum', 'Tether USDt', 'BNB', 'Solana', 'XRP', 'USDC', 'Cardano', 'Dogecoin', 'Avalanche', 'TRON', 'Chainlink', 'Polkadot', 'Toncoin', 'Polygon', 'Dai', 'Shiba Inu', 'Litecoin', 'Internet Computer', 'Bitcoin Cash']

# def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
#     kb = [
#         KeyboardButton(text=item) for item in items
#         ]
    # return ReplyKeyboardMarkup(keyboard=[kb])

def make_row_keyboard(items):
    builder = ReplyKeyboardBuilder()
    for i in items:
        builder.add(types.KeyboardButton(text=i))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)

class TrackingOrder(StatesGroup):
    choosing_currencies = State()
    choosing_time = State()


@dp.message(Command("start"))
async def start(message: types.Message):
 
    await message.answer(
'''
    Hello! 
I am a modern bot for tracking cryptocurrencies. I can:
- tracking the cryptocurrencies
- send you currency data on a schedule

Click Go! button or write it! 
    ''', reply_markup=make_row_keyboard(['Go!', 'Need help']))


@dp.message(StateFilter(None), F.text=='Go!')
async def cmd_currencies(message: types.Message, state: FSMContext):
    await message.answer(
        text='Which currencies you want to tracking?', 
        reply_markup=make_row_keyboard(currencies))
    await state.set_state(TrackingOrder.choosing_currencies)


@dp.message(
    TrackingOrder.choosing_currencies,
    F.text.in_(currencies)
)
async def currencies_chosen(message: Message, state: FSMContext):
    await state.update_data(choosen_currencies=message.text)
    await message.answer(
        text='Ok,set time:  first hours, after minutes',
        
        reply_markup=make_row_keyboard([h for h in range(0,25)], [m for m in range(0,61)])
    )
    await state.set_state(TrackingOrder.choosing_time)


@dp.message(TrackingOrder.choosing_currencies, F.text.in_(currencies))
async def final(message: Message, state: FSMContext):
    data = await state.get_data()

    await message.answer(text=f'{message.text} {data["choosen_currencies"]}')




# сделать:
# 1. пользователь выбирает валюты
# 2. подтверждает выбор
# 3. данные идут в бд как ['user_name', 'user_id', 'requests', 'request_time']
# 4. бот пробегается по базе данных и парсит данные, и отправляет значение валюты пользователю по расписанию

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())