from aiogram import Router, F
from aiogram import types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove
from dataclasses import dataclass

from kbs.make_keyboard import make_keyboard
from utils.model import new_order

from handlers.constants import (
    SUPPORTED_CURRENCIES,
    DAY_MODES,
    CONSENT,
    START_BUTTONS
    )

from handlers.constants import (
    TEXT_WHICH_CURRENCIES, 
    TEXT_WHAT_TIME,
    TEXT_CONFIRM_OR_NOT,
    TEXT_ORDER_WAS_SET,
    TEXT_ORDER_NOT_CREATED
)


router = Router()


class OrderTracking(StatesGroup):
    currency_selected = State()
    time_selected = State()
    user_has_confirmed = State()


@router.message(StateFilter(None), F.text=='Go')
async def order_start(message: types.Message, state: FSMContext):
    await message.answer(
        text=TEXT_WHICH_CURRENCIES, 
        reply_markup=make_keyboard(SUPPORTED_CURRENCIES))
    await state.set_state(OrderTracking.currency_selected)


@router.message(
    OrderTracking.currency_selected,
    F.text.in_(SUPPORTED_CURRENCIES)
)
async def time_choosing(message: Message, state: FSMContext):
    await state.update_data(chosen_currency=message.text)
    await message.answer(
        text=TEXT_WHAT_TIME,
        reply_markup=make_keyboard(DAY_MODES)
    )
    await state.set_state(OrderTracking.time_selected)


@router.message(
    OrderTracking.time_selected,
    F.text.in_(DAY_MODES)
)
async def confirming(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(
        text=TEXT_CONFIRM_OR_NOT,
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
        currency=data['chosen_currency'],
        time_=''.join([i for i in data['time'] if i.isdigit() or i.isalpha()]),
        confirm=True if data['confirm'] == 'Confirm' else False
    )

    if user_order.confirm:
        data = new_order(username=message.from_user.username, 
                  public_name=message.chat.id, 
                  currency=user_order.currency,
                  time_is_AM=user_order.time_=='12AM' 
                )

        await state.clear()
        await message.answer(text=TEXT_ORDER_WAS_SET,
            reply_markup=ReplyKeyboardRemove())

    else:
        await state.clear()
        await message.answer(
        text=TEXT_ORDER_NOT_CREATED,
        reply_markup=make_keyboard(START_BUTTONS))