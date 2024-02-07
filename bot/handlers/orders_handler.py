from aiogram import Router, F
from aiogram import types

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from kbs.make_keyboard import make_keyboard
from handlers.constants import START_BUTTONS
from model import get_orders

router = Router()


__all__ = [
    'clear',
    'orders',
    'remove'
]

@router.message(StateFilter(None), Command('clear'))
async def clear_states(message: types.Message, state: FSMContext):
    await message.answer(
        text='Current orser was clear!',
        reply_markup=make_keyboard(START_BUTTONS))
    await state.clear() 


@router.message(StateFilter(None), Command('orders'))
async def get_orders_from_db(message: types.Message, state: FSMContext):
    await message.answer(text=f'List of your orders:{get_orders(public_name=message.chat.id)}')
    

@router.message(StateFilter(None), Command('remove'))
async def get_orders_from_db(message: types.Message, state: FSMContext):
    await message.answer(text=str(get_orders(public_name=message.chat.id)))