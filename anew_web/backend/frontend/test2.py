from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from States.data import drums_nav2, bass_nav2, vox_nav2, about_nav2, policy_nav2
from States.data import bass_nav_xpath,title_nav_xpath, geckoDriverPath
from States.data import localhost,drums_nav_xpath,vox_nav_xpath
from urllib.error import HTTPError as pageNotFound
from selenium.webdriver.common.by import By
from selenium import webdriver as web
import os

class webDriver:
    def __init__(self):
        self.driver = None
    def start_driver(self):
        firefox_options = web.FirefoxOptions()
        os.environ[
            "webdriver.firefox.driver"
            ] =  geckoDriverPath
        self.driver = web.Firefox(
            options=firefox_options        
        )
        self.driver.maximize_window()
    def start_browser(self):
        try:
            self.driver.get(localhost)
            print("Browser Activation")
        except pageNotFound as err:
            print(err,"Page Not Found")
    def nav_iterator(self):
        try:
            WDW(
                self.driver,
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH,title_nav_xpath
            )))
            self.driver.find_element(
                        By.XPATH,
            title_nav_xpath).click()
            print('title nav clicked')
            self.driver.implicitly_wait(3)
            self.driver.back()
            print('back selected')
        except ElementNotInteractableException as err:
            while err == True:
                if title_nav_xpath != self.driver.find_element(
                    By.XPATH,title_nav_xpath):
                    print(err,"Element Not Found")
                    self.driver.implicitly_wait(3)
                    WDW(
                        self.driver,
                        timeout=10).until(
                    EC.presence_of_element_located((
                    By.XPATH,title_nav_xpath
                    )))
                else: 
                    self.driver.find_element(
                        By.XPATH,
                    title_nav_xpath).click()
                    print('title nav clicked')
                    self.driver.implicitly_wait(3)
                    self.driver.back()
                    print('back selected')
                break
        try:
            WDW(
                self.driver,
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH,drums_nav_xpath
            )))
            self.driver.find_element(
                        By.XPATH,
            drums_nav_xpath).click()
            print('drums nav clicked')
            self.driver.implicitly_wait(3)
            self.driver.back()
            print('back selected')
        except ElementNotInteractableException as err:
            while err == True:
                if drums_nav_xpath != self.driver.find_element(
                    By.XPATH,drums_nav_xpath):
                    print(err,"Element Not Found")
                    self.driver.implicitly_wait(3)
                    WDW(
                        self.driver,
                        timeout=10).until(
                    EC.presence_of_element_located((
                    By.XPATH,drums_nav_xpath
                    )))
                else: 
                    self.driver.find_element(
                        By.XPATH,
                    drums_nav_xpath).click()
                    print('drums nav clicked')
                    self.driver.implicitly_wait(3)
                    self.driver.back()
                    print('back selected')
                break
        try:
            WDW(
                self.driver,
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH,bass_nav_xpath
            )))
            self.driver.find_element(
                        By.XPATH,
            bass_nav_xpath).click()
            print('bass nav clicked')
            self.driver.implicitly_wait(3)
            self.driver.back()
            print('back selected')
        except NoSuchElementException as err:
            while err == True:
                if bass_nav_xpath != self.driver.find_element(
                    By.XPATH,bass_nav_xpath):
                    print(err,"Element Not Found")
                    self.driver.implicitly_wait(3)
                    WDW(
                        self.driver,
                        timeout=10).until(
                    EC.presence_of_element_located((
                    By.XPATH,bass_nav_xpath
                    )))
                else: 
                    self.driver.find_element(
                        By.XPATH,
                    bass_nav_xpath).click()
                    print('bass nav clicked')
                    self.driver.implicitly_wait(3)
                    self.driver.back()
                    print('back selected')
                break
        try:
            WDW(
                self.driver,
                timeout=10).until(
            EC.presence_of_element_located((
            By.XPATH,vox_nav_xpath
            )))
            self.driver.find_element(
                        By.XPATH,
            vox_nav_xpath).click()
            print('vox nav clicked')
            self.driver.implicitly_wait(3)
            self.driver.back()
            print('back selected')
        except NoSuchElementException as err:
            while err == True:
                if vox_nav_xpath != self.driver.find_element(
                    By.XPATH,vox_nav_xpath):
                    print(err,"Element Not Found")
                    self.driver.implicitly_wait(3)
                    WDW(
                        self.driver,
                        timeout=10).until(
                    EC.presence_of_element_located((
                    By.XPATH,vox_nav_xpath
                    )))
                else: 
                    self.driver.find_element(
                        By.XPATH,
                    vox_nav_xpath).click()
                    print('vox nav clicked')
                    self.driver.implicitly_wait(3)
                break
    def close_driver(self):
        print('quit driver')
        self.driver.close()


if __name__ == "__main__" :
    counter = 80
    func = webDriver()
    func.start_driver()
    func.start_browser()
    for i in range(counter):
        func.nav_iterator()
    counter +=1
    func.close_driver()
