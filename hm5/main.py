import sys
import asyncio
from services.exchange_service import ExchangeRateService
from exceptions import InvalidDaysCount

async def main():
    try:
        if len(sys.argv) != 2:
            raise InvalidDaysCount("Потрібно вказати кількість днів (1–10) як аргумент.")

        days = int(sys.argv[1])
        if not 1 <= days <= 10:
            raise InvalidDaysCount("Кількість днів повинна бути від 1 до 10.")

        service = ExchangeRateService()
        result = await service.get_exchange_rates(days)
        print(result)

    except ValueError:
        print("Невірний формат аргументу. Введіть число.")
    except InvalidDaysCount as e:
        print(e)
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
