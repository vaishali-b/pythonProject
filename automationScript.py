import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import sys

class LoggerWriter(object):
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message != '\n':
            self.logger.log(self.level, message)

    def flush(self):
        pass
        
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s  - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',filename='out.log')

stdout_logger = logging.getLogger('STDOUT')
sl = LoggerWriter(stdout_logger, logging.INFO)
sys.stdout = sl

stderr_logger = logging.getLogger('STDERR')
sl = LoggerWriter(stderr_logger, logging.ERROR)
sys.stderr = sl

class CustomSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("ADD CHROME DRIVER PATH")
        self.driver.maximize_window()
        
    try:
        def test_search_in_amazon(self):
            url="https://www.amazon.com"
            driver = self.driver
            driver.get(url)
            timeout = 8 # seconds
            print('Testing the website {}'.format(url))
            self.assertIn("Amazon", driver.title)
            driver.implicitly_wait(timeout)
            
            nav_menu = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='nav-link-accountList']/span[1]")))
            option_hover = ActionChains(driver).move_to_element(nav_menu)
            option_hover.perform()
            print("Clicking on Navigation Menu")
            
            flyout_sign_in = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='nav-flyout-ya-signin']/a/span")))
            flyout_sign_in.click()
            print("Clicking on Sign In Button")
            
            email = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ap_email']")))
            email.send_keys("ENTER EMAIL ID")
            
            continue_btn = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='continue']")))
            continue_btn.click()
            print("Entered Email")
            
            password = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ap_password']")))
            password.send_keys("ENTER PASSWORD")
            print("Entered Password")
            
            sign_in_btn = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='signInSubmit']")))
            sign_in_btn.click()
            print("Signed In to the website")
            
            
            search_bar = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='twotabsearchtextbox']")))
            search_bar.send_keys("Laptop")
            print("Searching for product Laptop")
            
            
            search_icon = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='nav-search']/form/div[2]/div/input")))
            search_icon.click()
            print("Search icon clicked")
            
            
            apply_brand = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='p_89/Acer']/span/a/span")))
            apply_brand.click()
            print("Applying brand filter")
            
            
            user_icon = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='nav-link-accountList']/span[1]")))
            hover = ActionChains(driver).move_to_element(user_icon)
            hover.perform()
            print("Clicked on User Icon")
            
            log_out = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,"//*[@id='nav-item-signout']/span")))
            log_out.click()
            print("Successfully logged out")
            
            
            
    except Exception as err:
        logging.exception("message")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
