from aiogram import Router, F
from aiogram import types

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dataclasses import dataclass

from kbs.make_keyboard import make_keyboard

router = Router()

currencies = ['Bitcoin', 'Ethereum', 'Tether USDt', 'BNB', 'Solana', 'XRP', 'USDC', 'Cardano', 'Dogecoin', 'Avalanche', 'TRON', 'Chainlink', 'Polkadot', 'Toncoin', 'Polygon', 'Dai', 'Shiba Inu', 'Litecoin', 'Internet Computer', 'Bitcoin Cash']
times = ['12AM 🌞', '12PM 🌑']
confirmations = ['Confirm', 'I do not confirm']

class OrderTracking(StatesGroup):
    currencies_choosed = State()
    time_choosed = State()
    user_has_confirmed = State()



@router.message(StateFilter(None), F.text=='go')
async def order_start(message: types.Message, state: FSMContext):
    await message.answer(
        text='Which currencies you want to tracking?', 
        reply_markup=make_keyboard(currencies))
    await state.set_state(OrderTracking.currencies_choosed)


@router.message(
    OrderTracking.currencies_choosed,
    F.text.in_(currencies)
)
async def time_choosing(message: Message, state: FSMContext):
    await state.update_data(choosen_currencies=message.text)
    await message.answer(
        text='At what time?',
        reply_markup=make_keyboard(times)
    )
    await state.set_state(OrderTracking.time_choosed)


@router.message(
    OrderTracking.time_choosed,
    F.text.in_(times)
)
async def confirming(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(
        text='Do you confirm?',
        reply_markup=make_keyboard(confirmations)
    )
    await state.set_state(OrderTracking.user_has_confirmed)




@router.message(OrderTracking.user_has_confirmed, F.text.in_(confirmations))
async def confirmation_of_data(message: Message, state: FSMContext):
    await state.update_data(confirm=message.text)
   
    @dataclass
    class UserOrder:
        currency: str 
        time_: str 
        confirm: bool 

    
    data = await state.get_data()

    user_order = UserOrder(
        currency=data['choosen_currencies'],
        time_=''.join([i for i in data['time'] if i.isdigit() or i.isalpha()]),
        confirm=True if data['confirm'] == 'Confirm' else False
    )

    print(user_order)

    if user_order.confirm:
        await message.answer(
        text=f"""
    You choosed: \n
    Currency: {user_order.currency}\n 
    Time: {user_order.time_}"""
    )

        await state.clear()
    else:
        await message.answer(
        text=f"Sorry, your order not created!",
        reply_markup=make_keyboard())


            
@router.message(StateFilter(None), Command('clear'))
async def clear_states(message: types.Message, state: FSMContext):
    await message.answer(
        text='All was remove!',
        reply_markup=make_keyboard(['go', 'help']))
    await state.clear()  
