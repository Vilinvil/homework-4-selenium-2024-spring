import pytest

from cases import BaseCase
from ui.pages.base_page import BasePage, PageWithRedirectWindow


class TestFooter(BaseCase):
    def test_display(self):
        self.base_page.hover_footer()

        assert self.base_page.find_footer_wrapper_language()
        assert self.base_page.find_footer_logo_ok()
        assert self.base_page.find_footer_logo_tg()
        assert self.base_page.find_footer_logo_vk()
        assert self.base_page.find_footer_button_cases()
        assert self.base_page.find_footer_about_company()
        assert self.base_page.find_footer_button_cabinet()
        assert self.base_page.find_footer_button_documents()
        assert self.base_page.find_footer_button_events()
        assert self.base_page.find_footer_button_experts()
        assert self.base_page.find_footer_button_help()
        assert self.base_page.find_footer_button_insights()
        assert self.base_page.find_footer_button_monetization()
        assert self.base_page.find_footer_button_news()
        assert self.base_page.find_footer_logo_vk_business()

    @pytest.mark.parametrize(
        'click_to,url,redirect',
        [
            pytest.param(
                BasePage.click_footer_button_news, 'https://ads.vk.com/news'
            ),
            pytest.param(
                BasePage.click_footer_button_insights, 'https://ads.vk.com/insights'
            ),
            pytest.param(
                BasePage.click_footer_button_events, 'https://ads.vk.com/events'
            ),
            pytest.param(
                BasePage.click_footer_button_documents, 'https://ads.vk.com/documents'
            ),
            pytest.param(
                BasePage.click_footer_button_cases, 'https://ads.vk.com/cases'
            ),
            pytest.param(
                BasePage.click_footer_button_help, 'https://ads.vk.com/help'
            ),
        ],
    )
    def test_open_pages(self, click_to, url):
        click_to(self.base_page)

        assert self.base_page.check_url(url)

    @pytest.mark.parametrize(
        'redirect_to,url',
        [
            pytest.param(
                BasePage.redirect_footer_button_experts, 'https://expert.vk.com/'
            ),
            pytest.param(
                BasePage.redirect_footer_button_monetization, 'https://ads.vk.com/partner'
            ),
            pytest.param(
                BasePage.redirect_footer_button_vk_business, 'https://vk.company/ru/company/business/'
            ),
            pytest.param(
                BasePage.redirect_footer_button_logo_vk, 'https://vk.com/vk_ads'
            ),
            pytest.param(
                BasePage.redirect_footer_button_logo_ok, 'https://ok.ru/group/64279825940712'
            ),
            pytest.param(
                BasePage.redirect_footer_button_logo_tg, 'https://t.me/vk_ads'
            ),
            pytest.param(
                BasePage.redirect_footer_button_about_company, 'https://vk.company/ru/'
            ),
        ],
    )
    def test_open_pages(self, redirect_to, url):
        page_with_redirect = PageWithRedirectWindow(self.driver)
        redirect_to(self.base_page, page_with_redirect)

        self.base_page.check_url(url)

    @pytest.mark.parametrize(
        'click_language,text_value',
        [
            pytest.param(
                BasePage.click_footer_button_language_ru, 'RU'
            ),
            pytest.param(
                BasePage.click_footer_button_language_en, 'EN'
            ),
        ],
    )
    def test_language_wrapped_buttons(self, click_language, text_value):
        self.base_page.click_footer_wrapper_language()

        click_language(self.base_page)
        assert self.base_page.get_footer_language() == text_value
