from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
import os.path
import requests
import shutil
import os
import glob
import random
from PIL import Image
import pickle
from getmac import get_mac_address as gma
import pkg_resources.py2_warn




with open('config.json', 'r') as f:
    data = json.load(f)


class login:
    def __init__(self):
        #self.driver = webdriver.Chrome('.\chromedriver')
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver')

    def login(self):
        #  window_before =ghgyh
        driver = self.driver
        driver.get("https://www.pinterest.com/")
        time.sleep(1)

    

    def follow( self) : 
        driver = self.driver 
        driver.get('https://www.pinterest.com/dogstrust/')
        checker = input('Start Following ') 
        if(checker) : 
            for i in range(10) :   
                form_element = driver.find_element_by_xpath("//button[@class='RCK Hsu USg adn CCY czT Vxj aZc Zr3 hA- Il7 Jrn hNT BG7 NTm KhY']")
                form_element.click()


    

    

    def start(self):
      #  window_before =ghgyh
        driver = self.driver
        driver.delete_all_cookies()
        url = 'https://www.pinterest.com/'
        driver.get(url)
        if os.path.isfile(os.path.join(os.getcwd(), "cookies.pkl")):

            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
            self.follow()

        else:
            logged = self.login()
            checker = input('Log Your Account')
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

            if checker:
                    self.follow()
                    time.sleep(5)


if __name__ == "__main__":
    """r = requests.get('http://samacyc.pythonanywhere.com/api/checker')
    checker = False
    for mac in r.json() : 
        if gma() == mac['mac'] :
            checker = True

    if checker :
        """
    test = login()
        
    test.start()
    # print(data['watermark'])
    #test.set_watermark(os.path.join(os.getcwd(), "input.jpg"))
