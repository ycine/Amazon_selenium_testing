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
                "//a[@href='https://aws.amazon.com/marketplace/?nc2=h_ql_mp']")))
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(to_marketplace).perform()
        
        print('Sukces - Amazon marketplace - marketplace label')


    def move_to_operating_systems(self):

        wait_for_operating_systems_to_load = WebDriverWait(self.driver, 55).until(EC.visibility_of_all_elements_located((By.XPATH,
        "//div[@class='m-nav-panel-wrapper m-transitioned']")))
        

        # wait_for_operating_systems_to_load_COMPONENT = WebDriverWait(self.driver, 55).until(EC.visibility_of_all_elements_located((By.XPATH,
        # "//div[@id='m-nav-panel-marketplace']")))


        
        to_operating_systems = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html[1]/body[1]/header[1]/div[1]/div[2]/div[7]/div[1]/div[1]/div[2]/div[1]/a[1]"))).click()
        # REL PATH  //a[contains(text(),'Operating Systems »')]
        print('Sukces - Amazon marketplace - operating systems')


    def select_dropdown_menu(self):
        to_select_dropdown = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "//span[@class='awsui_arrow_18eso_20dwt_97']//span[@class='awsui_icon_h11ix_1pphm_98 awsui_size-normal-mapped-height_h11ix_1pphm_151 awsui_size-normal_h11ix_1pphm_147 awsui_variant-normal_h11ix_1pphm_219']"))).click()

        print('Sukces - Amazon marketplace - select dropdown')


    def select_aws_customer_rating(self):
        to_aws_customer_rating = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/div[1]/div/div/div/div/div/section/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[3]/div[2]/div/div/div/ul/li[4]/div[1]/div/span/span/span/span"))).click()

        print('Sukces - Amazon marketplace - select aws customer rating')

    
    def find_all_operating_systems_offers(self):
        # get_elements = self.driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div/section/section/div/div/div[2]/div/awsui-table/div/div[3]/table/tbody/tr[1]/td[2]/span/div/div[2]/h4/a')
        # get_elements[0].click()
        wait_for_operating_systems_to_load = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/div[1]/div/div/div/div/div/section/div/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/div[2]/h2/div")))
        content = self.driver.find_elements(By.CLASS_NAME, '''_1gBynetuXXCnY2Ps4E7y1J''')
        # awsui_link_4c84z_16m2q_93 _3HyXlFIpamoFLblSS8id4Q awsui_variant-secondary_4c84z_16m2q_140 awsui_font-size-body-m_4c84z_16m2q_414
        # awsui_root_18wu0_1tu1m_93 awsui_box_18wu0_1tu1m_207 awsui_p-right-xxs_18wu0_1tu1m_563 awsui_color-default_18wu0_1tu1m_207 awsui_font-size-default_18wu0_1tu1m_223 awsui_font-weight-default_18wu0_1tu1m_263
        # print(content[3].get_attribute('href'))
        cv = content[3].find_element(By.CSS_SELECTOR,'a').get_attribute('href')
        print(cv)
        # print(content[0])
       
        # for i in enumerate(content, start=0):
        #     print(i)
        

        # links_hrefs = [link.get_property('href') for link in content if link.get_property('href') != None]
        links_hrefs = [link.find_element(By.CSS_SELECTOR,'a').get_attribute('href') for link in content if link.find_element(By.CSS_SELECTOR,'a').get_attribute('href') != None]
        # print(links_hrefs)

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



      