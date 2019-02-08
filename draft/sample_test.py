from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class TestPage:
    def test_1(self):
        print("1")
        assert 1 == 1

    def test_selectBooking(self):
        hotel_сheckbox = "//div[@id='filter_hoteltype']//span[contains(text(),'Hotels')]/ancestor::a"
        available_properties_сheckbox = "div#filter_out_of_stock a"
        fillterNotification = "p.sr-filter-heading"

        driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        wait = WebDriverWait(driver, 10)

        # home page. fillSearchFieldsAndSubmit("Los Angeles")
        driver.get("https://booking.com")
        driver.find_element_by_css_selector("input[type='search']").send_keys("Los Angeles")
        driver.find_element_by_css_selector("div[data-mode='checkin']").click()
        driver.find_element_by_xpath("//div[text()='March 2019']/following::table[@class]/tbody/tr[3]/td[4]").click()
        driver.find_element_by_css_selector("div[data-mode='checkin']").click()
        driver.find_element_by_css_selector("button[class*=searchbox]").submit()
        # assert header
        # search page filter by Avalible hotels
        if driver.find_element_by_xpath(hotel_сheckbox).is_selected():
            driver.find_element_by_xpath(hotel_сheckbox).click()
        if driver.find_element_by_css_selector(available_properties_сheckbox):
            driver.find_element_by_css_selector(available_properties_сheckbox).click()
        notification_text = "Filters have been applied"
        # wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, fillterNotification), notification_text))

        # search page select One of top three hotels
        #

        driver.quit()
