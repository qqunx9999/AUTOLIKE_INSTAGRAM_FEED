from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from bs4 import BeautifulSoup as b
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import getpages
import login,schedule

driver = 0
#Set up your account and chrome driver path here
#---------------------------------------------------------------------------------------
username = "email@domain.com"
password = "Password"
CHROMEDRIVER_PATH = 'Your Chrome Driver Path'
driver = 0
#---------------------------------------------------------------------------------------


def main():
    global driver
    print("Running script..")
    CHROME_PATH = '/usr/bin/google-chrome'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options) if(input("Running on background (y/n) : ").lower()=="y") else webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    #driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options) if("y"=="y") else webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    l = login.Login(driver,username,password)
    l.signin()
    # driver.get("https://www.instagram.com/python.learning/")
    # gp = getpages.Getpages(driver)
    # gp.get_followers()
    # sleep(60)
schedule.every().day.at("15:10").do(main)
schedule.every().day.at("22:00").do(main)
if __name__ == '__main__':
    main()
