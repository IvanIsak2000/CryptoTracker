from aiogram import Router, F
from aiogram import types

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from kbs.make_keyboard import make_keyboard

router = Router()

currencies = ['Bitcoin', 'Ethereum', 'Tether USDt', 'BNB', 'Solana', 'XRP', 'USDC', 'Cardano', 'Dogecoin', 'Avalanche', 'TRON', 'Chainlink', 'Polkadot', 'Toncoin', 'Polygon', 'Dai', 'Shiba Inu', 'Litecoin', 'Internet Computer', 'Bitcoin Cash']

class TrackingOrder(StatesGroup):
    choosing_currencies = State()
    choosing_time = State()


@router.message(StateFilter(None), F.text=='Go!')
async def cmd_currencies(message: types.Message, state: FSMContext):
    await message.answer(
        text='Which currencies you want to tracking?', 
        reply_markup=make_keyboard(currencies))
    await state.set_state(TrackingOrder.choosing_currencies)


@router.message(
    TrackingOrder.choosing_currencies,
    F.text.in_(currencies)
)
async def currencies_chosen(message: Message, state: FSMContext):
    await state.update_data(choosen_currencies=message.text)
    await message.reply('')


    await state.set_state(TrackingOrder.choosing_time)


@router.message(TrackingOrder.choosing_currencies, F.text.in_(currencies))
async def final(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(text=f'{message.text} {data["choosen_currencies"]}')

    