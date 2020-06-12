from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from bs4 import BeautifulSoup as b
from selenium.webdriver import ActionChains
from time import sleep

class Pageint:
    def __init__(self,driver):
        self.driver = driver