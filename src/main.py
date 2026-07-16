from api import get_data_format, get_voting
from save_data import get_file_name, save, get_members_file_name
from src.save_data import DATA_DIR
import json

TERM = 10

def get_data(year: int, month: int) -> None:
    date_from, date_to = get_data_format(year, month)
    data = get_voting(TERM, date_from, date_to)
    file_path = save(data, get_file_name(year, month))
    print(f"Raw voting file saved in: {file_path}")

def get_members(term=TERM) -> None:
    data = get_voting(term)
    file_path = save(data, get_members_file_name(term))
    print(f"Members file saved in: {file_path}")