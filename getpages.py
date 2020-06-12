from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from bs4 import BeautifulSoup as b
from selenium.webdriver import ActionChains
from time import sleep

class Getpages:
    def __init__(self,driver):
        self.driver = driver

    def get_followers(self):
        sleep(5)
        flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
        flw_btn.click()
        print("Clicked")
        popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/ul")))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)

    def open_first_picture(self):
        """ Method that opens the first picture on an Instagram profile page """
        try:
            self.driver.find_element_by_xpath("(//div[@class=\"eLAPa\"]//parent::a)[1]").click()
        except NoSuchElementException:
            print("Profile has no picture")



        #react-root > section > main > section > div > div:nth-child(2) > div > article:nth-child(1) > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg
#/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg
#react-root > section > main > section > div > div:nth-child(2) > div > article:nth-child(1) > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg