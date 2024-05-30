import pytest

from cases import LoggedNewUserCase, LoggedCase
from ui.pages.overview_page import OverviewNewUserPage, OverviewPage


class TestNewUserOverview(LoggedNewUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_user_overview(self, driver):
        self.overview_new_user_page = OverviewNewUserPage(self.driver)

    def test_display(self):
        self.overview_new_user_page.check_display_start_actions()


class TestOverview(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_overview(self, driver):
        self.overview_page = OverviewPage(self.driver)
        self.max_count_campaigns = 5

    def test_display(self):
        self.overview_page.check_display()

    def test_change_budget_date(self):
        budget_date_elem = self.overview_page.get_budget_date()
        assert budget_date_elem.text.find("cегодня")

        budget_date_elem.click()

        self.overview_page.click_budget_date_yesterday()

        budget_date_elem = self.overview_page.get_budget_date()
        assert budget_date_elem.text.find("Вчера")

    def test_modal_page_budget(self):
        self.overview_page.open_budget_replenish()
        self.overview_page.close_budget_replenish()

    def test_date_picker(self):
        self.overview_page.open_date_choose()
        self.overview_page.click_date_choose_today()
        self.overview_page.apply_date_choose()

        today_date = self.overview_page.get_date()

        self.overview_page.open_date_choose()
        self.overview_page.click_date_choose_yesterday()
        self.overview_page.apply_date_choose()

        yesterday_date = self.overview_page.get_date()

        assert (today_date - yesterday_date).days == 1

    @pytest.fixture(scope="function")
    def setup_choose_campaigns(self):
        self.overview_page.open_campaign_choose()

    @pytest.mark.parametrize('query, find_view',
                             [
                                 pytest.param(
                                     "asdfasdf",
                                     OverviewPage.find_sign_not_found_result_in_choose_campaign,
                                 ),
                                 pytest.param(
                                     "Кампания",
                                     OverviewPage.find_sign_found_result_in_choose_campaign,
                                 )
                             ], )
    def test_search_in_choose_campaigns(self,setup_choose_campaigns, query, find_view):
        self.overview_page.write_search_in_choose_campaign(query)

        assert find_view(self.overview_page)

    def test_tooltip_max_count_campaigns(self, setup_choose_campaigns):
        count_choose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        self.overview_page.activate_amount_campaigns(self.max_count_campaigns - count_choose_campaigns)

        self.overview_page.hover_checkbox_choose_campaign()
        assert self.overview_page.find_tooltip_max_choose_campaign()

    def test_reset_choose_campaigns(self, setup_choose_campaigns):
        cur_count_chose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        assert cur_count_chose_campaigns != 0

        self.overview_page.click_reset_choose_campaign()

        cur_count_chose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        assert cur_count_chose_campaigns == 0

        assert self.overview_page.is_not_display_checkboxes()

    def test_check_save_campaigns(self, setup_choose_campaigns):
        expected_count_chose_campaigns = 2

        self.overview_page.click_reset_choose_campaign()
        self.overview_page.activate_amount_campaigns(expected_count_chose_campaigns)

        self.overview_page.apply_campaign_choose()

        count_chosen_campaigns = self.overview_page.get_counter_choose_campaign_in_main_view()

        assert count_chosen_campaigns == expected_count_chose_campaigns

    def test_choose_settings_graph(self):
        begin_graph_settings = self.overview_page.get_graph_settings_text()

        self.overview_page.open_settings_graph()

        self.overview_page.click_choose_setting_graph_clicks()

        self.overview_page.apply_settings_graph()

        end_graph_settings = self.overview_page.get_graph_settings_text()

        assert begin_graph_settings != end_graph_settings and end_graph_settings == "Клики"
