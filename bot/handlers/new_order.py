from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove
from dataclasses import dataclass
import logging

from kbs.make_keyboard import make_keyboard
from model import new_order

from handlers.constants import SUPPORTED_CURRENCIES
from handlers.constants import DAY_MODES
from handlers.constants import CONSENT
from handlers.constants import START_BUTTONS

from handlers.constants import WHICH_CURRENCIES_TEXT
from handlers.constants import WHAT_TIME_TEXT
from handlers.constants import CONFIRM_OR_NOT_TEXT
from handlers.constants import ORDER_WAS_CLEAR_TEXT

router = Router()

logging.basicConfig(level=logging.INFO)

class OrderTracking(StatesGroup):
    SUPPORTED_CURRENCIES_choosed = State()
    time_choosed = State()
    user_has_confirmed = State()


@router.message(StateFilter(None), F.text=='Go')
async def order_start(message: types.Message, state: FSMContext):
    await message.answer(
        text=WHICH_CURRENCIES_TEXT, 
        reply_markup=make_keyboard(SUPPORTED_CURRENCIES))
    await state.set_state(OrderTracking.SUPPORTED_CURRENCIES_choosed)


@router.message(
    OrderTracking.SUPPORTED_CURRENCIES_choosed,
    F.text.in_(SUPPORTED_CURRENCIES)
)
async def time_choosing(message: Message, state: FSMContext):
    await state.update_data(choosen_currency=message.text)
    await message.answer(
        text=WHAT_TIME_TEXT,
        reply_markup=make_keyboard(DAY_MODES)
    )
    await state.set_state(OrderTracking.time_choosed)


@router.message(
    OrderTracking.time_choosed,
    F.text.in_(DAY_MODES)
)
async def confirming(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(
        text=CONFIRM_OR_NOT_TEXT,
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
        currency=data['choosen_currency'],
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