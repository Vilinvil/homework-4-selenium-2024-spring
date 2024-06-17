from selenium.webdriver.common.by import By


class CatalogLocators:
    BUTTON_CREATE_CATALOG = (By.XPATH, '//span[text()="Создать каталог"]')
    BUTTON_CONFIRM_CREATE_CATALOG = (By.XPATH, '(//span[text()="Создать каталог"])[2]')
    BUTTON_BY_HAND = (By.XPATH, '//h4[text()="Вручную"]')
    INPUT_TYPE_FEED = (By.XPATH, '//input[contains(@class, "vkuiCustomSelectInput__el")]')
    OPTION_AUTO = (By.XPATH, '//*[text()="Авто"]')
    FILE_INPUT = (By.XPATH, '//input[@type="file"]')
    MODAL_VIEW_TRAINING = (By.XPATH, '//*[text()="Хотите пройти обучение?"]')
    CHOOSE_NO = (By.XPATH, '//*[text()="Не сейчас"]')
    INPUT_CATALOG_NAME = (By.XPATH, '//input[@data-testid="catalogName-input"]')
    CATALOG_NAME_HEADER = (By.XPATH, '//h4')
    BUTTON_GOODS = (By.XPATH, '//span[text()="Товары"]')
    BUTTON_SETTINGS = (By.XPATH, '//span[text()="Настройки" and @class="vkuiButton__content"]')
    BUTTON_DELETE = (By.XPATH, '//span[text()="Удалить каталог"]')
    BUTTON_CONFIRM_DELETE = (By.XPATH, '//span[text()="Удалить"]')
    TEXT_NOT_FOUND = (By.XPATH, '//*[text()="Ничего не нашлось"]')
    TO_EVENTS = (By.XPATH, '//span[text()="События"]')
    FEED_OR_COMMUNITY = (By.XPATH, '//h4[text()="Фид или сообщество"]')
    INPUT_LINKS = (By.XPATH, '//input[@placeholder="Введите ссылку на фид или сообщество с товарами ВКонтакте"]')
    SELECT_UPDATE_PERIOD = (By.XPATH, '//input[@data-testid="catalogPeriod-select"]')
    UPDATE_PERIOD_SPAN = (By.XPATH,
                          '(//span[@class="vkuiTypography vkuiTypography--normalize vkuiTypography--weight-3 vkuiInfoRow vkuiHeadline--sizeY-compact vkuiHeadline--level-1"])[2]')

    @staticmethod
    def CHOOSE_PERIOD(period="1 час"):
        return By.XPATH, f'//*[text()="{period}"]'

    @staticmethod
    def BUTTON_OPEN_GOOD(item_name):
        return By.XPATH, f'//h5[text()="{item_name}"]'

    CLOSE_GOOD = By.XPATH, '//button[@aria-label="Close"]'

    @staticmethod
    def INFO_FIELD(i):
        return (By.XPATH,
                f"(//span[@class='vkuiTypography vkuiTypography--normalize vkuiTypography--weight-3 vkuiInfoRow "
                f"vkuiHeadline--sizeY-none vkuiHeadline--level-1'])[{i}]")

    SEARCH_FIELD = By.XPATH, '//input[@placeholder="Поиск"]'

    @staticmethod
    def ITEM_NAME(i=1):
        return By.XPATH, f'(//h5[contains(@class, "NameCell_itemName__gLQr9")])[{i}]'

    @staticmethod
    def ITEM_ID(i=1):
        return By.XPATH, f'(//span[contains(@class, "NameCell_itemId__QBh7+")])[{i}]'
