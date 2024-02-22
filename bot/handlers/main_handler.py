from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from kbs.make_keyboard import make_keyboard
from utils.model import get_orders, remove_orders

from handlers.constants import WELCOME_TEXT
from handlers.constants import START_BUTTONS
from handlers.constants import MODERATORS
from handlers.constants import ORDER_WAS_CLEAR_TEXT

router = Router()


__all__ = [
    'start',
    'help',       
    'orders',
    'remove'
]


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(WELCOME_TEXT, reply_markup=make_keyboard(START_BUTTONS))

  
@router.message(Command('help'))
async def help(message: types.Message):
    await message.answer(
        text='\n'.join([i for i in MODERATORS]))


@router.message(StateFilter(None), Command('orders'))
async def get_orders_from_db(message: types.Message, state: FSMContext):
    await message.answer(text=f'List of your orders:{get_orders(public_name=message.chat.id)}')
    

@router.message(StateFilter(None), Command('remove'))
async def get_orders_from_db(message: types.Message, state: FSMContext):
    remove_orders(public_name=message.chat.id)
    await message.answer(text='Your orders was removed!',
        reply_markup=make_keyboard(START_BUTTONS))
    
@router.message(Command('clear'))
async def clear_states(message: types.Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=ORDER_WAS_CLEAR_TEXT,
        reply_markup=make_keyboard(START_BUTTONS))