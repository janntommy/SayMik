import calendar
import requests

SEJM_URL = "https://api.sejm.gov.pl/sejm"

def get_data_format(year: int, month: int) -> tuple[str, str]:
    last_month_day = calendar.monthrange(year, month)[1]
    date_from = f"{year}-{month:02d}-01"
    date_to = f"{year}-{month:02d}-{last_month_day}"
    return date_from, date_to

def get_voting(term: int, date_from: str, date_to: str) -> str:
    url = f"{SEJM_URL}/term{term}/votings/search"
    response = requests.get(url, params={"dateFrom": date_from, "dateTo": date_to})
    response.raise_for_status()
    return response.text