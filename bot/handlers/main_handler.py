from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from kbs.make_keyboard import make_keyboard
from kbs.make_inline_keyboard import make_inline_keyboard
from utils.model import get_orders
from utils.model import remove_one_order
from utils.model import remove_orders

from handlers.constants import START_BUTTONS
from handlers.constants import MODERATORS

from handlers.constants import TEXT_WELCOME
from handlers.constants import TEXT_ORDER_WAS_CLEAR
from handlers.constants import TEXT_ONE_ORDER_HAS_BEEN_DELETED
from handlers.constants import TEXT_ALL_ORDERS_HAS_BEEN_DELETED

router = Router()


__COMMANDS__ = [
    'start',
    'help',       
    'orders',
    'remove'
    'clear'
]


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(TEXT_WELCOME, 
    reply_markup=make_keyboard(START_BUTTONS))

  
@router.message(Command('help'))
async def help(message: types.Message):
    await message.answer(
        text='\n'.join([i for i in MODERATORS]))


@router.message(StateFilter(None), Command('orders'))
async def get_orders_from_db(message: types.Message, state: FSMContext):
    await message.answer(text=f'List of your orders:', 
                         reply_markup=make_inline_keyboard(get_orders(public_name=message.chat.id))
    )
    
    
@router.callback_query(lambda d: d.data.startswith('to_remove:'))
async def remove_order(callback: types.CallbackQuery):
    currency_to_remove = callback.data.split(":")[1]

    remove_one_order(
        public_name=callback.message.chat.id,
        currency=currency_to_remove
    )

    await callback.answer(
    text=TEXT_ONE_ORDER_HAS_BEEN_DELETED,
    show_alert=True,
    reply_markup=make_inline_keyboard(get_orders(
        public_name=callback.message.chat.id))
    )


@router.message(StateFilter(None), Command('remove'))
async def remove_all_orders(message: types.Message, state: FSMContext):
    remove_orders(public_name=message.chat.id)
    await message.answer(text=TEXT_ALL_ORDERS_HAS_BEEN_DELETED,
        reply_markup=make_keyboard(START_BUTTONS)
    )
    

@router.message(Command('clear'))
async def clear_states(message: types.Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=TEXT_ORDER_WAS_CLEAR,
        reply_markup=make_keyboard(START_BUTTONS)
    )