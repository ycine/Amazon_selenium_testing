from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Amazon_main_page import Amazon_base_page
from Amazon_learn import Amazon_learn
from Amazon_training import Amazon_training
from Amazon_marketplace import Amazon_marketplace




# TEST BASE PAGE
# ----------------------------------------------------------------
# strona_glowna_1 = Amazon_base_page().call_webpage()
# print('-----------------ZAKONCZONO-------------------')
# ----------------------------------------------------------------


# TEST LEARN
# ----------------------------------------------------------------
# amazon_learn = Amazon_learn()
# amazon_learn.learn_label()
# amazon_learn.move_to_introduction_to_aws()
# amazon_learn.accept_all_cookies()
# amazon_learn.learn_more_about_aws_infrastructure()
# amazon_learn.get_infrastructure_cities()
# print('-----------------ZAKONCZONO-------------------')
# ----------------------------------------------------------------


# TEST TRAINING
# ----------------------------------------------------------------
amazon_training = Amazon_training()
amazon_training.learn_label()
amazon_training.move_to_training()
amazon_training.explore_digital_training()
amazon_training.free_learn_content()
amazon_training.accept_all_cookies()
amazon_training.aws_cloud_practitoner_essentials()
amazon_training.switch_tab_aws_skill_builder()
amazon_training.aws_cloud_practitoner_essentials_enroll()
print('-----------------ZAKONCZONO-------------------')
# ----------------------------------------------------------------


# TEST MARKETPLACE
# ----------------------------------------------------------------
# amazon_marketplace = Amazon_marketplace()
# amazon_marketplace.move_to_marketplace()
# amazon_marketplace.move_to_operating_systems()
# amazon_marketplace.accept_all_cookies()
# amazon_marketplace.select_dropdown_menu()
# amazon_marketplace.select_aws_customer_rating()
# amazon_marketplace.find_all_operating_systems_offers()
# print('-----------------ZAKONCZONO-------------------')
# ----------------------------------------------------------------