from __future__ import print_function

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from multiprocessing import Process
from threading import Thread
import multiprocessing
import time
import nexmo

#actions = ActionChains(browser) 

"""
driver = webdriver.Firefox()
driver.get('https://youtu.be/RYb2dokhZUs')
element = driver.find_element_by_class_name('style-scope ytd-player')
element.click()
"""

def function () : 
    driver = webdriver.Firefox()
    driver.get('https://www.youtube.com/watch?v=wiJckTdiW5o')
    element = driver.find_element_by_class_name('style-scope ytd-player')
    element.click()
    time.sleep(3)
    driver.close()


def final () : 
    actions = []

    for i in range(3) : 
        actions.append(Process(target=function , args=[]))

    for P in actions : 
        P.start() 


'''if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    for i in range(10) : 
        final() '''
from telesign.messaging import MessagingClient

customer_id = "DADE1E06-9E95-4D3D-B99E-FE4349B7B8AF"
api_key = "e89yfTY8y1w34LOCIJXrzPSO2s6LU2pF/hOPr4Ai786sN9XtfulEBeQgUcNJMqbgI73njn/5tvOG299BTW5MpA=="

phone_number = "212766981866"
message = "TEST"
message_type = "MKT"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(phone_number, message, message_type)
print(response.status_code)
print(response.json)