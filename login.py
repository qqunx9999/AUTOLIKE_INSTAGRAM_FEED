from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from bs4 import BeautifulSoup as b
from selenium.webdriver import ActionChains
from time import sleep

class Login:
    def __init__(self,driver,username,password):
        self.driver = driver
        self.username = username
        self.password = password
    def signin(self):
        print("opening")
        self.driver.get('https://www.instagram.com/')
        # uid = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")))
        # uid.click()
        # uid.send_keys(self.username)
        self.write("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input",self.username)
        self.write("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input",self.password)
        self.write("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div")
        self.write("#react-root > section > main > div > div > div > div > button")
        self.write("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        self.like_feed()


    def like_feed(self):
        count = 0
        t = 0
        a = 0
        b = 0
        while(b<=5):
            t+=1
            sleep(3)
            #hearts = self.driver.find_elements_by_xpath("//button[@class='dCJp8 afkep coreSpriteHeartOpen _0mzm-' and @aria-label='Like']")
            #hearts = self.driver.find_elements_by_xpath("//button[@class='dCJp8 afkep coreSpriteHeartOpen _0mzm-']")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.maximize_window()
            #hearts = self.driver.find_elements_by_xpath('//span[@class="fr66n"]/svg[]')
            #hearts = self.driver.find_elements_by_xpath('//avg[@aria-label="Like"]')
            hearts = self.driver.find_elements_by_xpath('//span[@class="fr66n"]//*[@aria-label="Like"][@class="_8-yf5 "]')
            sleep(5) if(len(hearts)==0) else sleep(1)
            print(f"Run {t} time generate for {len(hearts)} likes")
            for h in range(len(hearts)):
                try:
                    ActionChains(self.driver).move_to_element(hearts[h]).click(hearts[h]).perform()
                except Exception:
                    pass
            if(len(hearts)==0):
                a+=1
            if(a>=5):
                a = 0
                b+=1
                self.driver.get('https://www.instagram.com/')
                print("reset")
        print(f"Ending")

    def write(self,content,text=""):
        try:
            uid = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,content)))
        except Exception:
            return 0
        uid.click()
        uid.send_keys(text) if len(text)>0 else 0
