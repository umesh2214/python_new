import time

import pytest


@pytest.mark.skip
class Test_registration:
    def test_registration(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver= webdriver.Chrome()
        driver.get("https://automation.credence.in/shop")

        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("umesh")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("umesh1428@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("22149987")
        driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys("22149987")
        time.sleep(10)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("registration test case pass")
            assert True
        except:
            print("registration test case pass")
            assert False
        time.sleep(10)

