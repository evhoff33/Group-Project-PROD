import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        user = "testuser"
        pwd = "test123"
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        # Click the "Players" link
        driver.find_element(By.XPATH, "//a[contains(., 'Players')]").click()
        time.sleep(5)

        # Click on "Shai Gilgeous-Alexander" link
        driver.find_element(By.LINK_TEXT, "Shai Gilgeous-Alexander").click()
        time.sleep(5)

        try:
            # Click on "OKC Thunder" link
            driver.find_element(By.LINK_TEXT, "OKC Thunder").click()
            time.sleep(5)
        except NoSuchElementException:
            self.fail("Failed to click on OKC Thunder")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
