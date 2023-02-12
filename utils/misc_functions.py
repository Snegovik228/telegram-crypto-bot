# - *- coding: utf- 8 - *-
import aiohttp


# Асинхронный парсинг
async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


# Функция принимает название крипты и в каком фиате ее выводить
async def get_course(currency_crypto, currency_fiat):
    response = await get(
        f'https://min-api.cryptocompare.com/data/price?fsym={currency_crypto}&tsyms={currency_fiat}')

    return response[currency_fiat]


async def get_calc(currency_crypto):
    if currency_crypto == 'toncoin'.upper():
        response = await get(
            'https://ton.org/getpriceg/')
    print(currency_crypto)
    return response[currency_crypto]
