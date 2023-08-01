import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()

class Test_adding_to_cart:
    def test_login(self):

        driver.get("https://automation.credence.in/shop")
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("umesh1428@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("22149987")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    def test_adding_to(self):
        driver.find_element(By.XPATH, "//h3[normalize-space()='Electric Guitar']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a[2]").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH, "//h3[normalize-space()='Xbox One']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
    def test_select_items(self):
        item1=Select(driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/select[1]"))
        item1.select_by_index(1)
        item2=Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
        item2.select_by_index(2)
        item3=Select(driver.find_element(By.XPATH,"//tbody/tr[3]/td[3]/select[1]"))
        item3.select_by_index(4)
        driver.close()
    @pytest.mark.skip
    def test_checkout(self):
        driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-lg']").click()

        driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("umesh")
        driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("pawar")
        driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9276602825")
        driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("abcde")
        driver.find_element(By.XPATH,"//input[@id='zip']").send_keys("umesh")
        Select(driver.find_element(By.XPATH,"//select[@id='state']")).select_by_index(4)

        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("hrithik")
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        Select(driver.find_element(By.XPATH,"//select[@id='exp_year']")).select_by_index(5)
        Select(driver.find_element(By.XPATH,"//select[@id='exp_month']")).select_by_index(3)
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        try:
            driver.find_element(By.XPATH,"//h1[normalize-space()='Thank you.']")
            print("checkout case test is pass")
            driver.close()
            assert True
        except:
            print("checkout case test is fail")
            driver.close()
            assert False












