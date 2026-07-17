from api import get_data_format, get_voting, get_members as api_get_members
from save_data import get_file_name, get_members_file_name, save, DATA_DIR

TERM = 10

def get_data(year: int, month: int) -> None:
    date_from, date_to = get_data_format(year, month)
    data = get_voting(TERM, date_from, date_to)
    file_path = save(data, get_file_name(year, month))
    print(f"Raw voting file saved in: {file_path}")

def get_members(term=TERM) -> None:
    data = api_get_members(term)
    file_path = save(data, get_members_file_name(term))
    print(f"Members file saved in: {file_path}")