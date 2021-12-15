import json
import os
import random
from datetime import datetime
from typing import Dict, List, Generator

from faker import Faker

from conf import MODEL


# получить полный путь до корневой директории
basedir = os.path.abspath(os.path.dirname(__file__))


fake = Faker("ru_RU")


def get_title() -> str:
    """- Получить название книги"""
    with open(os.path.join(basedir, "books.txt"), encoding="utf-8") as file:
        lst = file.readlines()
        return random.choice(lst).strip()


def get_pages() -> int:
    """- получить количество страниц"""
    return fake.pyint()


def get_year() -> int:
    """- получить дату"""
    date: datetime = fake.date_object()
    return date.year


def get_isdn13() -> str:
    """- получить книжный номер"""
    return fake.bothify(text='###-#-#####-###-#')


def get_rating() -> float:
    """- получить книжный номер"""
    return round(random.uniform(0, 5), 1)


def get_price() -> float:
    """- получить книжный номер"""
    return round(random.uniform(500, 1500), 2)


def get_author() -> List[str]:
    """- получить книжный номер"""
    return [
        f"{fake.first_name()} {fake.last_name()}"
        for _ in range(random.randint(1, 3))
    ]


def get_data(pk: int) -> Generator:
    """- Полусить данные о книге"""
    yield {
        "model": MODEL,
        "pk": pk,
        "fields": {
            "title": get_title(),
            "year": get_year(),
            "pages": get_pages(),
            "isbn13": get_isdn13(),
            "rating": get_rating(),
            "price": get_price(),
            "author": get_author(),
        }
    }


def record_json(lst: List[dict]):
    """- записать файл json"""
    with open(os.path.join(basedir, "books.json"), mode="w", encoding="utf-8") as file:
        file.write(json.dumps(lst, indent=3, ensure_ascii=False))


def main():
    """- Точка входа"""
    count: int = 0  # счетчик итераций
    lst: List[dict] = []  # списко словарей

    # генерируем данные
    while True:

        count += 1

        # собираем данные в словарь
        lst.append(next(get_data(count)))

        if count >= 100:
            break

    record_json(lst)


if __name__ == '__main__':
    main()
