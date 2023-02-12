# - *- coding: utf- 8 - *-
import logging

from aiogram import Dispatcher

from data.config import admins

# Присылает сообщение о запуске бота
async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = f'Бот запущен!'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.Exception(err)
