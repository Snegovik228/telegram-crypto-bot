# - *- coding: utf- 8 - *-

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboard.inline.inline_kb_menu import ikb_crypto, ikb_crypto_eng, ikb_menu, ikb_fiat, ikb_fiat_eng
from loader import dp
# Выбор крипты для конвертации
from utils.misc_functions import get_calc


# ЭТА ФУНКЦИЯ ЕЩЕ НЕ ДОЛЕЛАНА!

@dp.callback_query_handler(text=['crypto_to_fiat', 'crypto_to_fiat_eng'])
async def select_crypto(call: CallbackQuery):
    if call.data == 'crypto_to_fiat':
        await call.message.edit_text('<b>♻ В какую валюту будем конвертировать?</b>', reply_markup=ikb_crypto)
    else:
        await call.message.edit_text('<b>♻ What currency will we convert to?</b>', reply_markup=ikb_crypto_eng)


# Выбор фиата для конвертации
@dp.callback_query_handler(text=['fiat_to_crypto', 'fiat_to_crypto_eng'])
async def select_fiat(call: CallbackQuery):
    if call.data == 'fiat_to_crypto':
        await call.message.edit_text('<b>♻ В какой фиат будем конвертировать?</b>', reply_markup=ikb_fiat)
    else:
        await call.message.edit_text('<b>♻ What fiat will we convert to?</b>', reply_markup=ikb_fiat_eng)


# Отмена конвертации
@dp.callback_query_handler(text=['convert_cancel', 'convert_cancel_eng'])
async def cancel_convert(call: CallbackQuery):
    if call.data == 'convert_cancel':
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    else:
        await call.message.edit_reply_markup(reply_markup=ikb_menu)


# После выбора валюты, предлагается ввести сумму
@dp.callback_query_handler(text_startswith='convert_crypto:')
async def send_message(call: CallbackQuery, state: FSMContext):
    get_crypto = call.data.split(':')[1]

    await state.update_data(here_select_crypto=get_crypto)
    await state.set_state('here_get_crypto')
    await call.message.edit_text(f'<b>Введите количество {get_crypto.upper()}:</b>')


@dp.message_handler(state='here_get_crypto')
async def get_convert(message: types.Message, state: FSMContext):
    get_crypto = await state.get_data()
    get_crypto = get_crypto['here_select_crypto']
    all_sum = ''

    if get_crypto == 'TONCOIN':
        rate_toncoin = await get_calc()
        all_sum = float(message.text) * rate_toncoin

    if all_sum:
        await state.finish()
        await message.answer(
            f'<b>✅ Результат конвертации</b> \n\n <code>{message.text}{get_crypto.upper()} = {all_sum}₽</code>')

# Подчет и вывод крипты в фиате
# @dp.message_handler(state='here_get_crypto')
# async def get_convert(message: types.Message, state: FSMContext):
#     get_crypto = await state.get_data()
#     get_crypto = get_crypto['here_select_crypto']
#     all_sum = ''
#     if get_crypto == 'btc':
#         rate_btc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_btc
#     elif get_crypto == 'eth':
#         rate_eth = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_eth
#     elif get_crypto == 'bnb':
#         rate_bnb = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_bnb
#     elif get_crypto == 'doge':
#         rate_doge = requests.get('https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_doge
#     elif get_crypto == 'ltc':
#         rate_ltc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_ltc
#     elif get_crypto == 'dash':
#         rate_dash = requests.get('https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_dash
#     elif get_crypto == 'xmr':
#         rate_xmr = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_xmr
#     elif get_crypto == 'rvn':
#         rate_rvn = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RVN&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_rvn
#     elif get_crypto == 'toncoin':
#         rate_toncoin = requests.get('https://min-api.cryptocompare.com/data/price?fsym=TONCOIN&tsyms=RUB').json()['RUB']
#         all_sum = float(message.text) * rate_toncoin

# if all_sum:
#     await state.finish()
#     await message.answer(
#         f'<b>✅ Результат конвертации</b> \n\n <code>{message.text}{get_crypto.upper()} = {all_sum}₽</code>')
