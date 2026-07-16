from api import get_data_format, get_voting
from save_data import get_file_name, save

TERM = 10

def get_data(year: int, month: int) -> None:
    date_from, date_to = get_data_format(year, month)
    data = get_voting(TERM, date_from, date_to)
    file_path = save(data, get_file_name(year, month))
    print(f"Saved in: {file_path}")

if __name__ == "__main__":
    get_data(2026, 6)