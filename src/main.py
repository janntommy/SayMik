from api import get_data_format, get_voting, get_members as api_get_members, get_voting_details
from save_data import get_file_name, get_members_file_name, save, DATA_DIR, get_details_file_name
import json
import time

TERM = 10

def get_data(year: int, month: int) -> None:
    date_from, date_to = get_data_format(year, month)
    data = get_voting(TERM, date_from, date_to)
    file_path = save(data, get_file_name(year, month))
    print(f"Raw voting file saved in: {file_path}")

def get_data_details(year: int, month: int) -> None:
    voting_file = DATA_DIR / get_file_name(year, month)
    if not voting_file.exists():
        raise ValueError(f"Voting file does not exist: {voting_file}")

    votings = json.loads(voting_file.read_text("utf-8"))
    details = []
    for voting in votings:
        sitting = voting["sitting"]
        voting_number = voting["votingNumber"]

        try:
            raw_details = get_voting_details(TERM, sitting, voting_number)
        except RuntimeError as err:
            print(err)
            continue

        if raw_details is None:
            continue

        details.append(json.loads(raw_details))
        time.sleep(0.5)

    file_path = save(json.dumps(details, ensure_ascii=False), get_details_file_name(year, month))
    print(f"Voting details file saved in: {file_path}")


def get_members(term=TERM) -> None:
    data = api_get_members(term)
    file_path = save(data, get_members_file_name(term))
    print(f"Members file saved in: {file_path}")