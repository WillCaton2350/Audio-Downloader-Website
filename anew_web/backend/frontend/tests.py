from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from urllib.error import HTTPError as pageNotFound
from frontend.States.data import *

class webDriver:
    def __init__(self):
        self.driver = None
    def start_driver(self):
        self.driver = web.Safari()
        self.driver.maximize_window()
    def start_browser(self):
        try:
            self.driver.get(localhost)
        except pageNotFound as err:
            if err == True:
                print(err,"Page Not Found")
                self.driver.implicitly_wait(3)
                self.driver.get(localhost)
            else:
                pass
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
            self.driver.implicitly_wait(3)
            self.driver.back()
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
                    self.driver.implicitly_wait(3)
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
            self.driver.implicitly_wait(3)
            self.driver.back()
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
                    self.driver.implicitly_wait(3)
                    self.driver.back()
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
            self.driver.implicitly_wait(3)
            self.driver.back()
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
                    self.driver.implicitly_wait(3)
                    self.driver.back()
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
            self.driver.implicitly_wait(3)
            self.driver.back()
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
                    self.driver.implicitly_wait(3)
                    self.driver.back()
                break