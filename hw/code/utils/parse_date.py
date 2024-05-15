from datetime import datetime

months = {
    "янв.": 1, "фев.": 2, "мар.": 3, "апр.": 4,
    "мая": 5, "июн.": 6, "июл.": 7, "авг.": 8,
    "сент.": 9, "окт.": 10, "нояб.": 11, "дек.": 12
}


def parse_date(date: str):
    day, month_name, year = date.split()
    month = months[month_name]

    date_result = datetime.strptime(f"{day} {month} {year}", "%d %m %Y")

    return date_result
