from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    driver = None
    hotel_сheckbox = "//div[@id='filter_hoteltype']//span[contains(text(),'Hotels')]/ancestor::a"
    available_properties_сheckbox = "div#filter_out_of_stock a"
    fillterNotification = "p.sr-filter-heading"

    def __init__(self, driver):
        self.driver = driver

    def filter_by_avalible_hotels(self):

        driver = self.driver
        if driver.find_element_by_xpath(self.hotel_сheckbox).is_selected():
            driver.find_element_by_xpath(self.hotel_сheckbox).click()
        if driver.find_element_by_css_selector(self.available_properties_сheckbox):
            driver.find_element_by_css_selector(self.available_properties_сheckbox).click()
        notification_text = "Filters have been applied"
        # wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, fillterNotification), notification_text))

        # search page select One of top three hotels
        #
