from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types

def make_keyboard(items):
    builder = ReplyKeyboardBuilder()
    for i in items:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)