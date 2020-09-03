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

    def checker(self, username):
        instagram = Instagram()
        medias = instagram.get_medias_from_feed(username)

        media = medias[0]
        return media

    def download(self, url, path, file_name, page):
        resp = requests.get(url, stream=True)
        # Open a local file with wb ( write binary ) permission.
        if not os.path.exists('./src/{}'.format(page)):
            os.makedirs('./src/{}'.format(page))
        local_file = open('{}.jpg'.format(path+file_name), 'wb')
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)
        # Remove the image url response object.
        del resp

    def set_watermark(self, original_image):
        path = os.path.join(os.getcwd(), 'watermarks')
        all_files = glob.glob(os.path.join(path, '*.png'))
        watermark_image = random.choice(all_files)
        base_image = Image.open(original_image)
        watermark = Image.open(watermark_image)
        width, height = base_image.size   # Get dimensions
        width1, height1 = watermark.size   # Get dimensions

        position = (int((width-width1)/2), int((height-height1)))
        base_image.paste(watermark, position, mask=watermark)
        base_image.save('./otput_image.jpg')

    def check(self):


        di_ = os.path.join(os.getcwd() , 'src') 
        images = os.listdir(di_) 
        if (len(images) >= 15) : 
            for i in range(15) : 
                print(os.path.join(di_ , images[i]))
                self.post(os.path.join(di_ , images[i]) , 'dfgbgf',
                            ('efgnbjbn'), (''))
        else : 
            for image in images : 
                print(os.path.join(di_ , image))
                self.post(os.path.join(di_ , image) , 'dfgbgf',
                            ('efgnbjbn'), (''))

        """try:    
            res = requests.get('https://5ro.fun/?action=display&bridge=Instagram&context=Username&u={}&media_type=picture&format=Json'.format(page))

            link = (res.json()['items'][0]['id'])

            id = link.split('/')
            short_code = (id[len(id) - 2])
            image_high_resolution_url = res.json()['items'][0]['content_text']
            # print(image.caption)
            if os.path.isfile(os.path.join(os.getcwd(), 'src', page, short_code + '.jpg')):
                print("Already Exist")
            else:
                self.download(image_high_resolution_url,
                              "./src/{}/".format(page), short_code, page)
                pic = short_code + '.jpg'
                path = os.path.join(os.getcwd(), 'src', page, pic)
                if (data['watermark']):

                    self.set_watermark(path)
                    path = os.path.join(os.getcwd(),'otput_image.jpg')
                self.post(path, 'dfgbgf',
                          ('efgnbjbn'), (''))
        except:
            print("failed Downlading image")
            return False """

    def post(self, path, link, Board, title):
        try:
            driver = self.driver
            driver.get("https://www.pinterest.com/pin-builder/")
            #pin = driver.find_element_by_xpath("//input[@accept ='image/bmp,image/gif,image/jpeg,image/png,image/tiff,image/webp,video/mp4,video/x-m4v,video/quicktime]")
            # pin.click()
            pic = driver.find_element_by_xpath(
                '//input[@id = "media-upload-input"]')
            pic.send_keys(os.path.join(os.getcwd(), path))
            time.sleep(random.randint(3, 5))
            direct = driver.find_element_by_xpath(
                '//textarea[@class = "TextArea__textArea TextArea__dark TextArea__hide_scrollbars TextArea__enabled TextArea__medium TextArea__nowrap"]')
            direct.click()
            direct.send_keys(random.choice(data['links']))
            try : 
                keyword = driver.find_element_by_xpath(
                    '//textarea[@placeholder ="Tell everyone what your Pin is about"]')
                keyword.send_keys(random.choice(data['description']))
            except : 
                pass 
            try : 
                keyword = driver.find_element_by_xpath(
                    '//textarea[@placeholder ="Add your title"]')
                keyword.send_keys(random.choice(data['titles']))
                keyword.send_keys(Keys.RETURN)
            except : 
                pass
            select = driver.find_element_by_xpath(
                '//button[@data-test-id="board-dropdown-select-button"]')
            select.click()
            time.sleep(5)
            board = driver.switch_to_active_element()
            board.click()
            Board = ("Animaux")
            board.send_keys(Board)
            board = driver.find_element_by_xpath(
                '//div[@title="{}"]'.format(Board))
            board.click()
            publish = driver.find_element_by_xpath(
                '//button[@data-test-id ="board-dropdown-save-button"]')
            publish.click()
            print('posted')
            os.remove(path)
            return True
        except:
            print('failed posting')
            return False

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
            self.check()
            time.sleep(5)

        else:
            logged = self.login()
            checker = input('Log Your Account')
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

            if checker:
                    self.check()
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
