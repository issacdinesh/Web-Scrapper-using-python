from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from datetime import datetime

import webbrowser

import schedule

import time


def task1():
    DRIVER_PATH = "chromedriver"

    options = Options()

    options.headless = True

    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    driver.get('https://www.qwiklabs.com/quests/128')

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    driver.quit()

    status = "offline"

    for post in soup.find_all('h3', 'headline-6 catalog-item__title js-catalog-item-title'):
        for poost in post.find_all('i', 'material-icons'):
            if(poost.text != "warning"):
                status = "online"
                date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(status, date_time)
                webbrowser.open_new_tab('status1.html')
            else:
                date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(status, date_time)    
    else:
        status = "online"
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(status, date_time)
        webbrowser.open_new_tab('status1.html')


schedule.every(20).minutes.do(task1)

task1()
while 1:
    schedule.run_pending()
    time.sleep(1)
