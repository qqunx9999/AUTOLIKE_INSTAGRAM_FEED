from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from bs4 import BeautifulSoup as b
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import getpages
import login

driver = 0
username = input("Enter your email/username of iG : ")
password = input("Enter your password of iG : ")




def main():
    global driver
    print("Running script..")
    CHROME_PATH = '/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/home/mnlenium/Downloads/Chrome-Driver/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
    l = login.Login(driver,username,password)
    l.signin()
    # driver.get("https://www.instagram.com/python.learning/")
    # gp = getpages.Getpages(driver)
    # gp.get_followers()
    # sleep(60)
if __name__ == '__main__':
    main()
