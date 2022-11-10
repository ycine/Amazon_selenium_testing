# -*- coding: windows-1250 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Amazon_main_page import Amazon_base_page
from Amazon_learn import Amazon_learn



class Amazon_marketplace(Amazon_learn):


    def move_to_marketplace(self):
        self.driver.get(self.sciezka)
        to_marketplace = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
                "/html/body/header/div[1]/div[1]/div[2]/nav/ul/li[7]/span/a")))
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(to_marketplace).perform()
        
        print('Sukces - Amazon marketplace - marketplace label')


    def move_to_operating_systems(self):
        to_operating_systems = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/header/div[1]/div[2]/div[7]/div/div/div[2]/div[1]/a"))).click()

        print('Sukces - Amazon marketplace - operating systems')


    def select_dropdown_menu(self):
        to_select_dropdown = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/div[1]/div/div/div/div/div/section/section/div/div/div[2]/div/awsui-table/div/div[2]/div[1]/div/span/div/div[2]/div/div/div/awsui-select/div/div/awsui-select-trigger/div/div"))).click()

        print('Sukces - Amazon marketplace - select dropdown')


    def select_aws_customer_rating(self):
        to_aws_customer_rating = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/div[1]/div/div/div/div/div/section/section/div/div/div[2]/div/awsui-table/div/div[2]/div[1]/div/span/div/div[2]/div/div/div/awsui-select/div/div/awsui-select-dropdown/div/div[1]/ul/li[4]/div/div/div/span"))).click()

        print('Sukces - Amazon marketplace - select aws customer rating')

    
    def find_all_operating_systems_offers(self):
        # get_elements = self.driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div/section/section/div/div/div[2]/div/awsui-table/div/div[3]/table/tbody/tr[1]/td[2]/span/div/div[2]/h4/a')
        # get_elements[0].click()

        content = self.driver.find_elements(By.CLASS_NAME, '''awsui-util-pr-xs''')
        # print(content)
        links_hrefs = [link.get_property('href') for link in content if link.get_property('href') != None]


        prices_list = {}
        for i in links_hrefs:
            # to_price_tag = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
            # "/html/body/div[2]/div[1]/div/div/div/div/div/section/section/div/div/div[2]/div/awsui-table/div/div[3]/table/tbody/tr[1]/td[2]/span/div/div[2]/h4/a")))
            # i.click()
            # to_price_tag = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
            # "/html/body/div[2]/div/div[2]/section[1]/div[3]/div/article[3]/div/div/div/p[1]")))
            
            print(i)
            self.driver.get(i)

            to_price_tag = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
            "/html/body/div[2]/div/div[2]/section[1]/div[3]/div/article[3]/div/div/div/p[1]")))

            to_operating_system_title = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
            "/html/body/div[2]/div/div[2]/section[1]/div[3]/div/article[2]/h1")))
            
            # prices_list.append(to_price_tag.text)
            prices_list[to_operating_system_title.text + ' --- '] = to_price_tag.text
            # self.driver.execute_script("window.history.go(-1)")

            # operating_systems_page = WebDriverWait(self.driver, 55).until(EC.visibility_of_element_located((By.XPATH,
            # "/html/body/div[2]/div[1]/div/div/div/div/div/section/section/div/div/div[2]/div/awsui-table/div/div[3]/table/tbody/tr[2]/td[2]/span/div/div[2]/h4/a")))

            # content1 = self.driver.find_elements(By.CLASS_NAME, 'awsui-util-pr-xs')
            # print(content1)
        


        for v,k in prices_list.items():
            print("System: {}  cena za godzinę pracy: {:<60}".format(v,k)) 
        # content[0].click()
        # print(get_elements)
        # to_aws_customer_rating = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((content[0]))).click()

        print('Sukces - Amazon marketplace - find all operating systems offers')



# tr.awsui-table-row:nth-child(1) > td:nth-child(2) > span:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h4:nth-child(1) > a:nth-child(1)
# html body div.content div.container div div#BEAGLE_WIDGET div.awsui div div#$mp-widget$ssvdieci428 section.aws-ui-widget section div.awsui-grid div.flexGrid--11xjah0QKI div.col--1OancJuiUr.main--3007mhLM3U div awsui-table.hide-thead.searchResults--1I8pgvtmfN div.awsui-table-inner.awsui-table-variant-default div.awsui-table-container table tbody tr.awsui-table-row td span div.productRow--15SbPnCqfx.awsui-util-mv-s div.productOverview--39Mo8vnnJA h4.awsui-util-pv-n a.awsui-util-pr-xs

# html body div.content div.container div div#BEAGLE_WIDGET div.awsui div div#$mp-widget$ssvdieci428 section.aws-ui-widget section div.awsui-grid div.flexGrid--11xjah0QKI div.col--1OancJuiUr.main--3007mhLM3U div awsui-table.hide-thead.searchResults--1I8pgvtmfN div.awsui-table-inner.awsui-table-variant-default div.awsui-table-container table tbody tr.awsui-table-row td span div.productRow--15SbPnCqfx.awsui-util-mv-s div.productOverview--39Mo8vnnJA h4.awsui-util-pv-n a.awsui-util-pr-xs



      