import asyncio
from pydantic import BaseModel
import aiogram
from aiogram.utils.text_decorations import html_decoration as hd

from logger import logger
from model import get_targets_for_sending

async def message_sender(bot: aiogram.client.bot.Bot):
    targets = get_targets_for_sending()
    fake_data = {'Polygon':10}
    completed = 0 
    for target in targets:
        try:
            await bot.send_message(chat_id=target.id,text=str(fake_data[target.request_currency]))
            completed += 1 
        except KeyError:
            pass
        except Exception as e :
            logger.error(e)

    logger.info(f'Orders[{completed}/{len(targets)}] was complied')
