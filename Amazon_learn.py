from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Amazon_main_page import Amazon_base_page




class Amazon_learn(Amazon_base_page):
    # def __init__(self) -> None:
    #     self.driver = webdriver.Firefox()
    #     self.sciezka = 'https://aws.amazon.com/'

    def learn_label(self):
        self.driver.get(self.sciezka)
        learn = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
                "//a[@href='/getting-started/?nc2=h_ql_le']")))
                
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(learn).perform()
        
        print('Sukces - Amazon learn - learn label')

    def move_to_introduction_to_aws(self):
        introduction_to_aws = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/header/div[1]/div[2]/div[5]/div[1]/div/div[1]/h3/a"))).click()

        print('Sukces - Amazon learn - move_to_introduction_to_aws')


    def accept_all_cookies(self):
        wait_for_learn_more_about_aws_infrastructure = WebDriverWait(self.driver, 55).until(EC.visibility_of_all_elements_located((By.XPATH,
        """//*[@id="awsccc-cb-content"]""")))

        accept_cookies = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div/div/div/button[2]"))).click()

        print('Sukces - accept all cookies')
        
    def learn_more_about_aws_infrastructure(self):
        learn_more_about_aws_infrastructure = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "//a[@class='m-gi-map-cta-link lb-txt-skt-blue']"))).click()

        print('Sukces - Amazon learn - learn_more_about_aws_infrastructure')


    def get_infrastructure_cities(self):

        show_modal_with_cities_wait = WebDriverWait(self.driver, 55).until(EC.visibility_of_all_elements_located((By.XPATH,
        "/html[1]/body[1]/div[2]/main[1]/div[4]/div[1]/div[1]/div[3]/div[1]/a[1]")))

        show_modal_with_cities = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html[1]/body[1]/div[2]/main[1]/div[4]/div[1]/div[1]/div[3]/div[1]/a[1]"))).click()

        cities_in_modal = WebDriverWait(self.driver, 55).until(EC.visibility_of_all_elements_located((By.XPATH,
        "/html[1]/body[1]/div[2]/main[1]/div[4]/div[1]/div[1]/div[3]/div[4]/div[1]/div[2]/section[1]/div[2]/p[4]")))

        print(cities_in_modal[0].text)


        def get_cities_from_driver(cities_in_modal):
            cities_list = []
            for i in range(len(cities_in_modal)):
                cities_list.append(cities_in_modal[i].text)
            cities_list_splited = cities_list[0].split('\n')
            # cities_list_splited = cities_list[0].split('\n')
            # cities_list_splited.pop(0)
            cities_list_splited2 = cities_list_splited[0].split(';')
            print(cities_list_splited2)
            for i in cities_list_splited2:
                print(i)
            return cities_list_splited2

        cities_names = get_cities_from_driver(cities_in_modal)

        close_modal = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "//div[@class='m-gi-map-modal-content lb-modal-content']//div[@class='lb-modal-close-container']//button[@class='lb-modal-close']"))).click()

        print('Sukces - Amazon learn - get_infrastructure_cities')
        
        
        