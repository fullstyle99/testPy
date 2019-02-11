from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    driver = None
    home_url = "https://booking.com"

    def __init__(self, driver):
        self.driver = driver

    def fill_in_search_fields_and_submit(self, search_value):
        self.driver.get(self.home_url)
        self.driver.find_element_by_css_selector("input[type='search']").send_keys(search_value)
        self.driver.find_element_by_css_selector("div[data-mode='checkin']").click()
        self.driver.find_element_by_xpath(
            "//div[text()='March 2019']/following::table[@class]/tbody/tr[3]/td[4]").click()
        self.driver.find_element_by_css_selector("div[data-mode='checkin']").click()
        self.driver.find_element_by_css_selector("button[class*=searchbox]").submit()

    def at_page(self):
        try:
            profile_logo_element = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located((By.ID, "header-details-user-fullname")))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False
