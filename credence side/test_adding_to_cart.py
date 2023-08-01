import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
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
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        driver.close()


