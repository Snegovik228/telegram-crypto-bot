# - *- coding: utf- 8 - *-
from aiogram import types

from filters import IsPrivate
from keyboard.default.menu_reply import kb_crypto
from loader import dp

# Хендлер отображающий стикер и сообщение при команде /start
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAIbQmJXP6kvhMQ8s8D5DEP1w1grGCA8AAJUAANBtVYMarf4xwiNAfojBA')
    await message.answer(f'Привет {message.from_user.full_name}, рады, что вы воспользовались нашим сервисом! \n\n'
                         f'💎Convert Crypto поможет Вам конвертировать из криптовалюты в фиатную валюту и обратно, по актуальному курсу биржы Binance.\n\n'
                         f'⚡Надежно и удобно\n\n'
                         f'<b>Приятного пользования 📈</b>',
                         reply_markup=kb_crypto)

# Хендлер для команды /help
@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         'Тебе нужна помощь?')
