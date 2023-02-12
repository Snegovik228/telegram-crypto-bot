# - *- coding: utf- 8 - *-
from aiogram import executor

import filters
from handlers import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    filters.setup(dp)

    await on_startup_notify(dp)

    await set_default_commands(dp)

    print('Бот запущен')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
