# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

# DEFAULT КНОПКИ
kb_crypto = ReplyKeyboardMarkup(resize_keyboard=True)
kb_crypto.row('📈 Актуальный курс', '📱 Калькулятор')
kb_crypto.row('⚙ Настройки', '⚠ О сервисе')

kb_crypto_eng = ReplyKeyboardMarkup(resize_keyboard=True)
kb_crypto_eng.row('📈 Сurrent exchange rate', '📱 Calculator')
kb_crypto_eng.row('⚙ Settings', '⚠ About')

kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back.row('🔙 Back')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row('💵 USD', '🪙 RUB', '💶 EUR')
kb_menu.row('🔙 Назад')

kb_menu_eng = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu_eng.row('💵 USD', '🪙 RUB', '💶 EUR')
kb_menu_eng.row('🔙 Back')

kb_settings = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_settings.row('💭 Изменить язык', '📝 Задать вопрос')
kb_settings.row('🔙 Назад')

kb_settings_eng = ReplyKeyboardMarkup(resize_keyboard=True)
kb_settings_eng.row('💭 Change the language', '📝 Ask a Question')
kb_settings_eng.row('🔙 Back')

lang_rus = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
lang_rus.row('🇷🇺 Русский', '🇺🇸 English')
lang_rus.row('🔙 Назад')
