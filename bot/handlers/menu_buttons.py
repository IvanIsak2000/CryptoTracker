from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types

from kbs.make_keyboard import make_keyboard


router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
        await message.answer(
'''
Hello! 

I am a modern bot for tracking cryptocurrencies. I can:
- tracking the cryptocurrencies
- send you currency data on a schedule

Click Go button!
    ''', reply_markup=make_keyboard(['go', 'Need help ❓'])
    )

  
@router.message(Command('help'))
async def help(message: types.Message):
    await message.answer(
        text='@IvanIsak2000'
        )

