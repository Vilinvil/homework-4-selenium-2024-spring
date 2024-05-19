from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")
    REGISTRATION_GO_BACK = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Назад")]')
    REGISTRATION_RUSSIAN_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Русский")]')
    REGISTRATION_ENGLISH_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"English")]')
    REGISTRATION_ADVERTISER_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Рекламодатель")]')
    REGISTRATION_AGENCY_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Агентство")]')
    REGISTRATION_COUNTRY_SELECT = (By.XPATH, '//*[@data-testid="country"]')
    REGISTRATION_CURRENCY_SELECT = (By.XPATH, '//*[@data-testid="currency"]')
    REGISTRATION_EMAIL_FIELD = (By.XPATH, '//*[@data-testid="email"]')
    REGISTRATION_INDIVIDUAL_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Физическое лицо")]')
    REGISTRATION_ENTITY_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Юридическое лицо")]')
    REGISTRATION_INN_FIELD = (By.XPATH, '//*[@name="inn"]')
    REGISTRATION_FIO_FIELD = (By.XPATH, '//*[@name="name"]')
    REGISTRATION_OFFER_CHECK_MARK = (By.NAME, "offer")
    REGISTRATION_MAILINGS_CHECK_MARK = (By.XPATH, '//*[contains(@class, "vkuiIcon") and @name != "offer"]')
    REGISTRATION_CREATE_BUTTON = (
        By.XPATH, '//*[@id="registration.new"]//*[contains(text(),"Создать кабинет")]')
    REGISTRATION_NO_OFFER_ALERT = (By.XPATH,
        '//*[@role="alert" and preceding-sibling::div[contains(@class, "registration_offerDesc__")]]')
    REGISTRATION_EMAIL_ALERT = (By.XPATH,
        '//*[@role="alert" and preceding-sibling::h5[text()="Email*"]]')
    REGISTRATION_INN_ALERT = (By.XPATH,
        '//*[@role="alert" and preceding-sibling::h5[text()="ИНН"]]')
    REGISTRATION_HEADER_TITLE = (By.XPATH, '//*[contains(@class, "HeaderNav_headerFormTitle")]')
    REGISTRATION_COUNTRY_SELECT_RUSSIA = (By.XPATH, '//*[contains(@class, "vkuiCustomSelectOption") and text()="Россия"]')
    REGISTRATION_COUNTRY_SELECT_BELARUS = (By.XPATH, '//*[contains(@class, "vkuiCustomSelectOption") and text()="Беларусь"]')
    REGISTRATION_CURRENCY_SELECT_RUB = (By.XPATH, '//*[@title="Российский рубль (RUB)"]')
    REGISTRATION_CURRENCY_SELECT_USD = (By.XPATH, '//*[@title="Доллар США (USD)"]')
    REGISTRATION_CURRENCY_SELECT_EUR = (By.XPATH, '//*[@title="Евро (EUR)"]')
