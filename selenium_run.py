from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException





class Amazon_Base:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.sciezka = 'https://aws.amazon.com/'


    def call_webpage(self):
        self.driver.get(self.sciezka)
        print('Wykonano..')







obj1 = Amazon_Base()
run1 = obj1.call_webpage()

    # wait = WebDriverWait(driver, 55).until(EC.element_to_be_clickable((By.XPATH,
    #                                                                 "/html[1]/body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]")))
# button = driver.find_element_by_xpath(
#     '/html[1]/body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]')
# button.click()
# # OLD
# # '/html/body/div[6]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td'

# ele2 = driver.find_element_by_xpath('''//*[@id="username"]''')
# ele2b = ele2.send_keys("marcin.wiaderkowicz@smartsolar.pl")
# ele3 = driver.find_element_by_xpath('''//*[@id="password"]''')
# ele3b = ele3.send_keys("smartmarcin456@")
# ele3c = driver.find_element_by_xpath(
#     "/html/body/form[2]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td").click()
    
#     # /html/body/form[2]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td
# print("Zakończono logowanie do Firmao.")