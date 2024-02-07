from aiogram import Router, F
from aiogram import types

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dataclasses import dataclass
from sqlalchemy import select

from kbs.make_keyboard import make_keyboard
from model import new_order
from handlers.constants import SUPPORTED_CURRENCIES
from handlers.constants import DAY_MODE
from handlers.constants import CONSENT
from handlers.constants import START_BUTTONS

router = Router()

class OrderTracking(StatesGroup):
    SUPPORTED_CURRENCIES_choosed = State()
    time_choosed = State()
    user_has_confirmed = State()


@router.message(StateFilter(None), F.text=='Go')
async def order_start(message: types.Message, state: FSMContext):
    await message.answer(
        text='Which currencies you want to tracking?', 
        reply_markup=make_keyboard(SUPPORTED_CURRENCIES))
    await state.set_state(OrderTracking.SUPPORTED_CURRENCIES_choosed)


@router.message(
    OrderTracking.SUPPORTED_CURRENCIES_choosed,
    F.text.in_(SUPPORTED_CURRENCIES)
)
async def time_choosing(message: Message, state: FSMContext):
    await state.update_data(choosen_SUPPORTED_CURRENCIES=message.text)
    await message.answer(
        text='At what time?',
        reply_markup=make_keyboard(DAY_MODE)
    )
    await state.set_state(OrderTracking.time_choosed)


@router.message(
    OrderTracking.time_choosed,
    F.text.in_(DAY_MODE)
)
async def confirming(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(
        text='Do you confirm?',
        reply_markup=make_keyboard(CONSENT)
    )
    await state.set_state(OrderTracking.user_has_confirmed)


@router.message(OrderTracking.user_has_confirmed, F.text.in_(CONSENT))
async def confirmation_of_data(message: Message, state: FSMContext):
    await state.update_data(confirm=message.text)
   
    @dataclass
    class UserOrder:
        currency: str 
        time_: str 
        confirm: bool 

    
    data = await state.get_data()

    user_order = UserOrder(
        currency=data['choosen_SUPPORTED_CURRENCIES'],
        time_=''.join([i for i in data['time'] if i.isdigit() or i.isalpha()]),
        confirm=True if data['confirm'] == 'Confirm' else False
    )

    if user_order.confirm:
        data = new_order(username=message.from_user.username, 
                  public_name=message.chat.id, 
                  currency=user_order.currency,
                  time_is_AM=user_order.time_=='12AM' )

        await state.clear()
        await message.answer(text=f'Your order was set!',
            reply_markup=ReplyKeyboardRemove())

    else:
        await state.clear()
        await message.answer(
        text=f"Sorry, your order not created! Please try again!",
        reply_markup=make_keyboard(START_BUTTONS))