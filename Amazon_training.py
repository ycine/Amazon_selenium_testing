from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Amazon_main_page import Amazon_base_page
from Amazon_learn import Amazon_learn




class Amazon_training(Amazon_learn):


    def move_to_training(self):
        to_training = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/header/div[1]/div[2]/div[5]/div[1]/div/div[3]/div[1]/a"))).click()

        print('Sukces - Amazon training - move to training')

    def explore_digital_training(self):
        to_explore_digital_training = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div/a"))).click()

        print('Sukces - Amazon training -  explore digital training  ')


    def free_learn_content(self):
        to_free_learn_content = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/main/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/a"))).click()

        print('Sukces - Amazon training -  free learn content  ')       


    def aws_cloud_practitoner_essentials(self):
        to_aws_cloud_practiioner_essentials = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/main/div[9]/div/div/div[2]/div/div[1]/div/a"))).click()

        print('Sukces - Amazon training -  aws cloud practitioner essentials')  

    def switch_tab_aws_skill_builder(self):
        # TO SLUZY DO SPRAWDZENIA OTWARTYCH ZAKLADEK W PRZEGLADARCE
        # get_handle = self.driver.window_handles
        # print(get_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # get_handle = self.driver.current_window_handle
        print('Sukces - zmieniono zakladke')


    def aws_cloud_practitoner_essentials_enroll(self):
        to_aws_cloud_practiioner_essentials_enroll = WebDriverWait(self.driver, 55).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[2]/div/div/div/doc-layout/div/main/div[2]/ng-component/div/course-content/div/div/div/div[2]/div[1]/enrollment/div/div[2]/ui-button-raised-primary/ui-button-raised/button"))).click()

        print('Sukces - Amazon training -  aws cloud practitioner essentials enroll')    






        



        

    
