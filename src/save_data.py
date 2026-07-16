from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1]/'data'/'raw'

def get_file_name(year: int, month: int) -> str:
    return f"voting_{year}_{month:02d}.json"

def get_details_file_name(year: int, month: int) -> str:
    return f"voting_details_{year}_{month:02d}.json"

def get_members_file_name(term: int) -> str:
    return f"members_term{term}.json"


def save(data: str, file_name: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_path = DATA_DIR / file_name
    file_path.write_text(data, encoding="utf-8")
    return file_path