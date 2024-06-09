from selenium.webdriver.common.by import By


class LeadFormsPageLocators:
    CREATE_FORM_BUTTON = (By.XPATH, '//span[text()="Создать лид-форму"]')
    SALES_BUTTON = (By.XPATH, '//span[text()="Скидка"]')
    BONUS_BUTTON = (By.XPATH, '//span[text()="Бонус"]')
    RUBLES_BUTTON = (By.XPATH, '//h4[text()="₽"]')
    RUBLES_BUTTON = (By.XPATH, '//h4[text()="₽"]')
    
    # DROP_MENU = (By.XPATH, '//span[text()="Активные" and @aria-live="polite"]')
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск"]')
    LEADFORMS_TAB = (By.XPATH, '//div[@aria-controls="leadforms"]')
    YCLIENTS_TAB = (By.XPATH, '//div[@aria-controls="yclients"]')
    SURVEYS_TAB = (By.XPATH, '//div[@aria-controls="surveys"]')

    INPUT_FORM_NAME = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    INPUT_COMPANY_NAME = (By.XPATH, '//input[@placeholder="Название компании"]')
    INPUT_HEADER = (By.XPATH, '//input[@placeholder="Текст заголовка"]')
    INPUT_SURVEYS_INFO = (By.XPATH, '//input[@placeholder="Краткое описание опроса"]')
    TEXTAREA_SURVEYS_DESCRIPTION = (By.XPATH, '//textarea[@placeholder="Расскажите о вашем опросе или предложении"]')
    SALE_VALUE_INPUT = (By.XPATH, '//span[@value="Бонус"]')


    CHOOSE_IMAGE_BUTTON = (By.XPATH, '//div[@data-testid="set-global-image]"')
    COMPACT_BUTTON = (By.XPATH, '//span[text()="Компактный"]')
    MORE_TEXT_BUTTON = (By.XPATH, '//span[text()="Больше текста"]')
    LEAD_MAGNITE_BUTTON = (By.XPATH, '//span[text()="Лид-магнит"]')

    CANCEL_BUTTON = (By.XPATH, '//span[text()="Отмена"]')
    CONTINUE_BUTTON = (By.XPATH, '//span[text()="Продолжить"]')
