from datetime import datetime, timedelta

def get_last_dates(days: int):
    today = datetime.now()
    return [(today - timedelta(days=i)).strftime("%d.%m.%Y") for i in range(days)]
