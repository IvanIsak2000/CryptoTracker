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

Click Go! button or write it! 
    ''', reply_markup=make_keyboard(['Go!', 'Need help']))

