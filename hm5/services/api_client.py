import aiohttp
from exceptions import APIRequestError

class PrivatBankAPIClient:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date={}"

    async def fetch_rates(self, date_str: str):
        url = self.BASE_URL.format(date_str)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise APIRequestError(f"Помилка HTTP {response.status}")
                    return await response.json()
        except aiohttp.ClientError as e:
            raise APIRequestError(f"Помилка мережі: {e}")
