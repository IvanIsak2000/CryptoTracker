from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def make_inline_keyboard(items):
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.row(types.InlineKeyboardButton(
            text=item['Currency'], callback_data=f'to_remove:{item["Currency"]}'))
    return builder.as_markup()