import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os
from dotenv import load_dotenv

load_dotenv()
BOT_KEY = os.environ.get('BOT_KEY')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_KEY)
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
    await message.answer('Choose', reply_markup=keyboard)

# сделать:
# 1. пользователь выбирает валюты
# 2. подтверждает выбор
# 3. данные идут в бд как ['user_name', 'user_id', 'requests', 'request_time']
# 4. бот пробегается по базе данных и парсит данные, и отправляет значение валюты пользователю по расписанию

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())