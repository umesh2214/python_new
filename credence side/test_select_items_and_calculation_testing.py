import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
    def test_select_items(self):
        item1=Select(driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/select[1]"))
        item1.select_by_index(1)
        item2=Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
        item2.select_by_index(2)
        item3=Select(driver.find_element(By.XPATH,"//tbody/tr[3]/td[3]/select[1]"))
        item3.select_by_index(4)
        time.sleep(40)
        l=len(driver.find_elements(By.XPATH,"//tbody/tr/td[4]"))

        items_ammount_list=[]
        for i in range(1,l-2):
            v=driver.find_element(By.XPATH,"//tbody/tr["+str(i)+"]/td[4]").text
            v1=v[1:]
            items_ammount_list.append(float(v1))

        total_items_ammount=round(sum(items_ammount_list),2)


        total_ammount_list=[]

        for j in range(l-2,l+1):
            p=driver.find_element(By.XPATH,"//tbody/tr["+str(j)+"]/td[4]").text
            p1=p[1:]
            p2=p1.replace(",","")
            total_ammount_list.append(float(p2))

        if total_items_ammount==total_ammount_list[0]:
            print("calculation test pass")
            driver.close()
            assert True
        else:
            print("calculation test fail")
            driver.close()
            assert False



