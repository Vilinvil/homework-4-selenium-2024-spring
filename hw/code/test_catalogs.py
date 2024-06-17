import pytest

from cases import LoggedCase
from ui.pages.catalogs_page import CatalogsPage

from selenium.common.exceptions import TimeoutException


class TestSurveysPage(LoggedCase):
    FEED_RELATIVE_FILEPATH = "hw/code/files/catalog_auto_google.csv"
    CATALOG_NAME = "Вручную"
    CATALOG_NAME_FEED = "Каталог 1"
    GOOD_NAME = "Москвич 3"
    ATTR_VALUE = {
        "Товар": "3",
        "Название товара": "Москвич 3",
        "Категория товара": "-",
        "Наличие": "В наличии",
        "Цена": "250,00 ₽",
        "Ссылка на сайт": "https://moskvich-auto.ru/models/moskvich-3",
        "Название": "Москвич 3",
        "Производитель": "Москвич",
        "Модель": "3",
        "Кузов": "suv",
        "Цвет кузова": "Белый",
        "Статус": "new",
        "Тип транспортного средства": "автомобиль",
        "VIN": "1A2BCDEF3GH456789",
        "Год производства": "2023",
        "Адрес": "3-я улица Строителей 55",
        "Состояние": "отличное",
        "Страна": "Россия",
        "Населённый пункт": "Казань",
        "Регион": "Республика Татарстан",
    }

    LINK = "https://vk.com/gangperm"
    UPDATE_PERIOD = "Период обновления\n1 час"

    GOOD_NAME_TO_SEARCH = "Куртка"
    GOOD_ID_TO_SEARCH = "9391898"

    @pytest.fixture(scope='function', autouse=True)
    def setup_surveys_page(self):
        self.main_page.open_catalogs()
        self.catalogs_page = CatalogsPage(self.driver)

    # @pytest.mark.skip
    def test_pos_case_by_hand(self):
        # Закрываем окно "Хотите пройти обучение?", если появляется
        self.catalogs_page.close_training_if_shown()

        # Создаем каталог
        self.catalogs_page.BUTTON_CREATE_CATALOG.clicks()
        self.catalogs_page.BUTTON_BY_HAND.clicks()
        self.catalogs_page.INPUT_CATALOG_NAME.write(self.CATALOG_NAME)
        self.catalogs_page.select_feed_auto()
        self.catalogs_page.load_feed_file(self.FEED_RELATIVE_FILEPATH)
        self.catalogs_page.BUTTON_CONFIRM_CREATE_CATALOG.clicks()

        # Переключаемся на товары
        self.catalogs_page.BUTTON_TO_GOODS.clicks()

        # Проверяем название каталога
        assert self.catalogs_page.CATALOG_HEADER_NAME == self.CATALOG_NAME

        # Ждем пока загрузится фид
        self.catalogs_page.NOT_FOUND_MESSAGE

        # Обновляем страницу каталога товаров
        self.catalogs_page.BUTTON_TO_EVENTS.clicks()
        self.catalogs_page.BUTTON_TO_GOODS.clicks()

        # Проверяем, что товар каталога имеет ожидаемые параметры
        self.catalogs_page.BUTTON_OPEN_GOOD(self.GOOD_NAME).clicks()
        i = 1
        for key, value in self.ATTR_VALUE.items():
            assert self.catalogs_page.INFO_FIELD(i) == f"{key}" + "\n" + f"{value}"
            i += 1

        self.catalogs_page.CLOSE_GOOD.clicks()

        # Удаляем каталог
        self.catalogs_page.BUTTON_SETTINGS.clicks()
        self.catalogs_page.BUTTON_DELETE.clicks()
        self.catalogs_page.BUTTON_CONFIRM_DELETE.clicks()

    def test_pos_case_feed(self):
        # Закрываем окно "Хотите пройти обучение?", если появляется
        self.catalogs_page.close_training_if_shown()

        # Создаем каталог
        self.catalogs_page.BUTTON_CREATE_CATALOG.clicks()
        self.catalogs_page.INPUT_CATALOG_NAME.write(self.CATALOG_NAME_FEED)
        self.catalogs_page.BUTTON_FEED_OR_COMMUNITY.clicks()
        self.catalogs_page.INPUT_LINKS.write(self.LINK)
        self.catalogs_page.SELECT_UPDATE_PERIOD.clicks()
        self.catalogs_page.UPDATE_PERIOD_OPTION('1 час').clicks()
        self.catalogs_page.BUTTON_CONFIRM_CREATE_CATALOG.clicks()

        # Проверяем период обновления
        try:
            assert self.catalogs_page.UPDATE_PERIOD_SPAN == self.UPDATE_PERIOD
        except TimeoutException:
            self.catalogs_page.BUTTON_CONFIRM_CREATE_CATALOG.clicks()
            assert self.catalogs_page.UPDATE_PERIOD_SPAN == self.UPDATE_PERIOD

        # Переключаемся на товары
        self.catalogs_page.BUTTON_TO_GOODS.clicks()

        # Проверяем название каталога
        assert self.catalogs_page.CATALOG_HEADER_NAME == "Товары – " + self.CATALOG_NAME_FEED

        # Ждем пока загрузится фид
        self.catalogs_page.NOT_FOUND_MESSAGE

        # Обновляем страницу каталога товаров
        self.catalogs_page.BUTTON_TO_EVENTS.clicks()
        self.catalogs_page.BUTTON_TO_GOODS.clicks()

        # Удаляем каталог
        self.catalogs_page.BUTTON_SETTINGS.clicks()
        self.catalogs_page.BUTTON_DELETE.clicks()
        self.catalogs_page.BUTTON_CONFIRM_DELETE.clicks()
