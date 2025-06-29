from services.api_client import PrivatBankAPIClient
from utils.date_utils import get_last_dates

class ExchangeRateService:
    def __init__(self):
        self.api_client = PrivatBankAPIClient()

    async def get_exchange_rates(self, days: int):
        dates = get_last_dates(days)
        results = []

        for date in dates:
            data = await self.api_client.fetch_rates(date)
            rate_entry = {
                date: {
                    "EUR": self._extract_currency(data, "EUR"),
                    "USD": self._extract_currency(data, "USD")
                }
            }
            results.append(rate_entry)

        return results

    def _extract_currency(self, data, currency_code):
        for rate in data.get("exchangeRate", []):
            if rate.get("currency") == currency_code:
                return {
                    "sale": rate.get("saleRate"),
                    "purchase": rate.get("purchaseRate")
                }
        return {"sale": None, "purchase": None}
