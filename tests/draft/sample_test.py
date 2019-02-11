from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from src.pages.home_page import HomePage
from src.pages.search_page import SearchPage


class TestPage:
    def test_1(self):
        print("1")
        assert 1 == 1

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)

    def test_selectBooking(self):
        self.home_page.fill_in_search_fields_and_submit("Los Angeles")
        # assert self.home_page.at_page()
        self.search_page.filter_by_avalible_hotels()

    def teardown_method(self):
        self.driver.close()
