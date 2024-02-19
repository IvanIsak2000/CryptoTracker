import asyncio
from model import get_targets_for_sending
from pydantic import BaseModel
import aiogram
from logger import logger


async def message_sender(bot: aiogram.client.bot.Bot):
    chat_id=5261974343
    await bot.send_message(chat_id=chat_id, text='Your data')
    logger.info('Data was send')
#     class User(BaseModel):
#         id: int
#         query_currency: str
#         currency_amount: float


#     for target in targets:
#         user = User(id=target.id, query_currency=target.currency, currency_amount=target.amount )
#         await bot.send_message(chat_id=user.id, text=user.query_currency+user.currency_amount) 
