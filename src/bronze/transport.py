from src.api import get_data_format, get_voting
from src.save_data import get_file_name

VOLUME_PATH = "/Volumes/db_saymik/bronze/raw_files"
TERM = 10

def transfer_to_unity(year: int, month: int) -> None:
    date_from, date_to = get_data_format(year, month)
    data = get_voting(10, date_from, date_to)

    file_path = f"{VOLUME_PATH}/{get_file_name(year, month)}"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)

    print(f"Data saved to: {file_path}")

def load_to_bronze(year: int, month: int) -> None:
    file_path = f"{VOLUME_PATH}/{get_file_name(year, month)}"
    table_name = f"db_saymik.bronze.votings_raw_{year}_{month:02d}"

    df = spark.read.json(file_path)
    df.write.format("delta").mode("overwrite").saveAsTable(table_name)

    print(f"Loaded {file_path} into {table_name}")


transfer_to_unity(2026, 6)
load_to_bronze(2026,6)
