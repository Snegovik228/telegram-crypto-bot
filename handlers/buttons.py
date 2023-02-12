# - *- coding: utf- 8 - *-
from datetime import date

import requests
from aiogram import types

from keyboard.default.menu_reply import kb_settings, kb_settings_eng, kb_menu, kb_menu_eng, kb_crypto, kb_crypto_eng, \
    lang_rus
from keyboard.inline import ikb_menu
from keyboard.inline.inline_kb_menu import ikb_menu_eng
from loader import dp
from utils.misc_functions import get_course


# Показывает актуальный курс в USD
@dp.message_handler(text='💵 USD')
async def rate_crypto_usd(message: types.Message):
    del_loading = await message.reply('♻ Получаем актуальный курс')

    await message.answer_photo(requests.get("https://imageup.ru/img64/4170277/rubli.jpg").content,
                               f"✅ Актуальный курс на:\n {date.today()}\n\n"
                               "<b>Валюта: USD\n\n"
                               f"🔸 BTC  =  <code>{await get_course('BTC', 'USD')}$</code>\n"
                               f"🔸 ETH  =  <code>{await get_course('ETH', 'USD')}$</code>\n"
                               f"🔸 BNB  =  <code>{await get_course('BNB', 'USD')}$</code>\n"
                               f"🔸 DOGE  =  <code>{await get_course('DOGE', 'USD')}$</code>\n"
                               f"🔸 LTC  =  <code>{await get_course('LTC', 'USD')}$</code>\n"
                               f"🔸 DASH  =  <code>{await get_course('DASH', 'USD')}$</code>\n"
                               f"🔸 XMR  =  <code>{await get_course('XMR', 'USD')}$</code>\n"
                               f"🔸 RVN  =  <code>{await get_course('RVN', 'USD')}$</code>\n"
                               f"🔸 TON  =  <code>{await get_course('TONCOIN', 'USD')}$</code></b>\n")

    await del_loading.delete()


# Показывает актуальный курс в RUB
@dp.message_handler(text='🪙 RUB')
async def rate_crypto_rub(message: types.Message):
    del_loading = await message.reply('♻ Получаем актуальный курс')

    await message.answer_photo(requests.get("https://imageup.ru/img228/4170278/dollary.jpg").content,
                               f"✅ Актуальный курс на:\n {date.today()}\n\n"
                               "<b>Валюта: RUB\n\n"
                               f"🔸 BTC  =  <code>{await get_course('BTC', 'RUB')}₽</code>\n"
                               f"🔸 ETH  =  <code>{await get_course('ETH', 'RUB')}₽</code>\n"
                               f"🔸 BNB  =  <code>{await get_course('BNB', 'RUB')}₽</code>\n"
                               f"🔸 DOGE  =  <code>{await get_course('DOGE', 'RUB')}₽</code>\n"
                               f"🔸 LTC  =  <code>{await get_course('LTC', 'RUB')}₽</code>\n"
                               f"🔸 DASH  =  <code>{await get_course('DASH', 'RUB')}₽</code>\n"
                               f"🔸 XMR  =  <code>{await get_course('XMR', 'RUB')}₽</code>\n"
                               f"🔸 RVN  =  <code>{await get_course('RVN', 'RUB')}₽</code>\n"
                               f"🔸 TON  =  <code>{await get_course('TONCOIN', 'RUB')}₽</code></b>\n")

    await del_loading.delete()


# Показывает актуальный курс в EUR
@dp.message_handler(text='💶 EUR')
async def rate_crypto_eur(message: types.Message):
    del_loading = await message.reply('♻ Получаем актуальный курс')

    await message.answer_photo(requests.get("https://imageup.ru/img194/4170279/evro.jpg").content,
                               f"✅ Актуальный курс на:\n {date.today()}\n\n"
                               "<b>Валюта: EUR\n\n"
                               f"🔸 BTC  =  <code>{await get_course('BTC', 'EUR')}€</code>\n"
                               f"🔸 ETH  =  <code>{await get_course('ETH', 'EUR')}€</code>\n"
                               f"🔸 BNB  =  <code>{await get_course('BNB', 'EUR')}€</code>\n"
                               f"🔸 DOGE  =  <code>{await get_course('DOGE', 'EUR')}€</code>\n"
                               f"🔸 LTC  =  <code>{await get_course('LTC', 'EUR')}€</code>\n"
                               f"🔸 DASH  =  <code>{await get_course('DASH', 'EUR')}€</code>\n"
                               f"🔸 XMR  =  <code>{await get_course('XMR', 'EUR')}€</code>\n"
                               f"🔸 RVN  =  <code>{await get_course('RVN', 'EUR')}€</code>\n"
                               f"🔸 TON  =  <code>{await get_course('TONCOIN', 'EUR')}€</code></b>\n")

    await del_loading.delete()


# Кнопка для выхода назад
@dp.message_handler(text=['🔙 Назад', '🔙 Back'])
async def command_back(message: types.Message):
    if message.text == '🔙 Назад':
        await message.answer('Переходим', reply_markup=kb_crypto)
    else:
        await message.answer('Loading', reply_markup=kb_crypto_eng)


# Кнопка калькулятора
@dp.message_handler(text=['📱 Калькулятор', '📱 Calculator'])
async def command_calculator(message: types.Message):
    if message.text == '📱 Калькулятор':
        await message.answer('👇 Выберите метод конвертации', reply_markup=ikb_menu)
    else:
        await message.answer('👇 Select conversion method', reply_markup=ikb_menu_eng)


# Кнопка настройки
@dp.message_handler(text=['⚙ Настройки', '⚙ Settings'])
async def command_settings(message: types.Message):
    if message.text == '⚙ Настройки':
        await message.answer('Переходим', reply_markup=kb_settings)
    else:
        await message.answer('Loading', reply_markup=kb_settings_eng)


# Кнопка о сервисе
@dp.message_handler(text=['⚠ О сервисе', '⚠ About'])
async def command_about(message: types.Message):
    if message.text == '⚠ О сервисе':
        await message.answer('<b>ConvertCrypto - сервис с актуальными курсами.\n\n'
                             'Узнать цену курса можно в 2 клика\n\n'
                             'Делать точные расчеты стало проще, благодаря калькулятору.\n\n'
                             'Подписывайся на наш телеграм канал и получай свежие сигналы</b>\n\n'
                             '<a href="t.me/convertinfo"><b>Подписаться</b></a>')
    else:
        await message.answer('<b>ConvertCrypto is a service with up-to-date rates.\n\n'
                             'You can find out the cost of the course in 2 clicks\n\n'
                             'Making accurate calculations has become easier thanks to the calculator.\n\n'
                             'Subscribe to our telegram channel and get fresh signals</b>\n\n'
                             '<a href="t.me/convertinfo"><b>Subscribe</b></a>')


# Кнопка для выбора изменения языка
@dp.message_handler(text=['💭 Изменить язык', '💭 Change the language'])
async def select_language(message: types.Message):
    if message.text == '💭 Изменить язык':
        await message.answer('Выберите необходимый язык', reply_markup=lang_rus)
    else:
        await message.answer('Choose the required language', reply_markup=lang_rus)


# Кнопка Задать вопрос
@dp.message_handler(text=['📝 Задать вопрос', '📝 Ask a Question'])
async def ask_question(message: types.Message):
    if message.text == '📝 Задать вопрос':
        await message.answer("<b>Спасибо, что выбрали нашего бота</b>\n\n"
                             f"Если у Вас возникли вопросы или технические трудности, "
                             f"при работе с ботом, будем рады обратной связи.\n\n"
                             f'<a href="t.me/snegdev">Связаться</a>', disable_web_page_preview=True)
    else:
        await message.answer("<b>Thank you for choosing our bot</b>\n\n"
                             f"If you have any questions or technical difficulties, "
                             f"when working with the bot, we will be glad to receive feedback.\n\n"
                             f'<a href="t.me/snegdev">Contact</a>', disable_web_page_preview=True)


# Выбор языка
@dp.message_handler(text=['🇷🇺 Русский', '🇺🇸 English'])
async def select_language(message: types.Message):
    if message.text == '🇷🇺 Русский':
        await message.answer("<b>Вы успешно сменили язык!</b>", reply_markup=kb_crypto)
    else:
        await message.answer("<b>You have successfully changed the language!</b>", reply_markup=kb_crypto_eng)


# Кнопка актуальный курс
@dp.message_handler(text=['📈 Актуальный курс', '📈 Сurrent exchange rate'])
async def actual_rate(message: types.Message):
    if message.text == '📈 Актуальный курс':
        await message.answer('👇 Выберите фиатную валюту', reply_markup=kb_menu)
    else:
        await message.answer('👇 Choose a fiat currency', reply_markup=kb_menu_eng)
