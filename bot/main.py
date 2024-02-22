import logging
import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import inspect

from utils.logger import logger
from utils.config import BOT_KEY
from handlers import new_order 
from handlers import main_handler
from utils.sending import message_sender

bot = Bot(token=BOT_KEY)
dp = Dispatcher()


async def bot_task(bot: bot, dp: dp):
    dp.include_routers(
        new_order.router,
        main_handler.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def sender_task(bot: bot):
    logger.info(f'{inspect.currentframe()} got bot object')
    scheduler = AsyncIOScheduler()
    scheduler.add_job(message_sender, 'interval', seconds=5, args=[bot])
    scheduler.start()
 

if __name__ == "__main__":
    logger.info('Program was start')
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(bot_task(bot, dp)),
        loop.create_task(sender_task(bot))
    ]
    loop.run_until_complete(asyncio.gather(*tasks))
    logger.info('Goodbye!\n---------------------------------------')