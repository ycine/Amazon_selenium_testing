from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# PONIZEJ TO DO DODANIA ROZSZERZENIA DO OKNA
# chrome_options = Options()
# chrome_options.add_extension('path_to_extension')

# driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options



class Amazon_base_page:
    def __init__(self) -> None:
        
        self.sciezka = 'https://aws.amazon.com/'  
        # self.xchro = r"C:\Users\HP\AppData\Roaming\Mozilla\Firefox\Profiles\y63d0pkl.default-release\extensions\{83efb7a7-cf21-4f94-840a-316f651053ef}.xpi"
        # self.options = Options()
        # self.options.headless = True
        # self.options(self.xchro)  
        self.driver = webdriver.Firefox()
        # self.driver.add_extension(self.xchro, temporary=True)
        

    def call_webpage(self):
        self.driver.get(self.sciezka)
        # learn_build_to_get_connected = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        # "/html/body/div[2]/main/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div[3]/div/div[2]/div/a/div[1]"))).click()
        print('Sukces ! - Amazon base page')



# obj1 = Amazon_base_page()
# obj1.call_webpage()
# run1 = obj1.learn_label()

# wait = WebDriverWait(driver, 55).until(EC.element_to_be_clickable((By.XPATH,
#      "/html[1]/body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]")))
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