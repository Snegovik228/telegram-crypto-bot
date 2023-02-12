# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ИНЛАЙН КНОПКИ, ФУНКЦИОНАЛ В ФАЙЛЕ user_convert.py
ikb_menu = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text='Криптовалюта 🔄 Фиат', callback_data='crypto_to_fiat'),
).add(
    InlineKeyboardButton(text='Фиат 🔄 Криптовалюта', callback_data='fiat_to_crypto'),
)

ikb_menu_eng = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text='Crypto 🔄 Fiat', callback_data='crypto_to_fiat_eng'),
).add(
    InlineKeyboardButton(text='Fiat 🔄 Crypto', callback_data='fiat_to_crypto_eng'),
)

convert_fiat = InlineKeyboardMarkup()
convert_fiat.row('💵 USD', '🪙 RUB', '💶 EUR')
convert_fiat.row('🔙 Back')

ikb_crypto = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text='️▫ BTC', callback_data='convert_crypto:btc'),
    InlineKeyboardButton(text='️▫ ETH', callback_data='convert_crypto:eth'),
    InlineKeyboardButton(text='️▫ BNB', callback_data='convert_crypto:bnb'),
    InlineKeyboardButton(text='️▫ DOGE', callback_data='convert_crypto:doge'),
    InlineKeyboardButton(text='️▫ LTC', callback_data='convert_crypto:ltc'),
    InlineKeyboardButton(text='️▫ DASH', callback_data='convert_crypto:dash'),
    InlineKeyboardButton(text='️▫ XMR', callback_data='convert_crypto:xmr'),
    InlineKeyboardButton(text='️▫ RVN', callback_data='convert_crypto:rvn'),
    InlineKeyboardButton(text='️▫ TON', callback_data='convert_crypto:toncoin'),
).add(
    InlineKeyboardButton(text='Отмена', callback_data='convert_cancel')
)

ikb_crypto_eng = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text='️▫ BTC', callback_data='convert_crypto:btc'),
    InlineKeyboardButton(text='️▫ ETH', callback_data='convert_crypto:eth'),
    InlineKeyboardButton(text='️▫ BNB', callback_data='convert_crypto:bnb'),
    InlineKeyboardButton(text='️▫ DOGE', callback_data='convert_crypto:doge'),
    InlineKeyboardButton(text='️▫ LTC', callback_data='convert_crypto:ltc'),
    InlineKeyboardButton(text='️▫ DASH', callback_data='convert_crypto:dash'),
    InlineKeyboardButton(text='️▫ XMR', callback_data='convert_crypto:xmr'),
    InlineKeyboardButton(text='️▫ RVN', callback_data='convert_crypto:rvn'),
    InlineKeyboardButton(text='️▫ TON', callback_data='convert_crypto:toncoin'),
).add(
    InlineKeyboardButton(text='Cancel', callback_data='convert_cancel_eng')
)

ikb_fiat = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text='️▫ BTC', callback_data='convert_crypto:btc'),
    InlineKeyboardButton(text='️▫ ETH', callback_data='convert_crypto:eth'),
    InlineKeyboardButton(text='️▫ BNB', callback_data='convert_crypto:bnb'),
    InlineKeyboardButton(text='️▫ DOGE', callback_data='convert_crypto:doge'),
    InlineKeyboardButton(text='️▫ LTC', callback_data='convert_crypto:ltc'),
    InlineKeyboardButton(text='️▫ DASH', callback_data='convert_crypto:dash'),
    InlineKeyboardButton(text='️▫ XMR', callback_data='convert_crypto:xmr'),
    InlineKeyboardButton(text='️▫ RVN', callback_data='convert_crypto:rvn'),
    InlineKeyboardButton(text='️▫ TON', callback_data='convert_crypto:toncoin'),
).add(
    InlineKeyboardButton(text='Отмена', callback_data='convert_cancel')
)

ikb_fiat_eng = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text='️▫ BTC', callback_data='convert_crypto:btc'),
    InlineKeyboardButton(text='️▫ ETH', callback_data='convert_crypto:eth'),
    InlineKeyboardButton(text='️▫ BNB', callback_data='convert_crypto:bnb'),
    InlineKeyboardButton(text='️▫ DOGE', callback_data='convert_crypto:doge'),
    InlineKeyboardButton(text='️▫ LTC', callback_data='convert_crypto:ltc'),
    InlineKeyboardButton(text='️▫ DASH', callback_data='convert_crypto:dash'),
    InlineKeyboardButton(text='️▫ XMR', callback_data='convert_crypto:xmr'),
    InlineKeyboardButton(text='️▫ RVN', callback_data='convert_crypto:rvn'),
    InlineKeyboardButton(text='️▫ TON', callback_data='convert_crypto:toncoin'),
).add(
    InlineKeyboardButton(text='Отмена', callback_data='convert_cancel')
)
