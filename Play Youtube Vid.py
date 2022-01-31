import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

Title = input("Enter the title of the Video: ")

PATH = 'C:\\Users\\Lenovo\\Desktop\\Progamming\\WebScrapping\\chromedriver.exe'
wd = webdriver.Chrome(PATH)
wd.maximize_window()
wd.implicitly_wait(20)
url = "https://www.youtube.com/"


def search_video(wd, name, site=url):
    wd.get(site)

    wd.find_element(By.NAME, "search_query").send_keys(name)
    print('Got into searchbox')
    wd.find_element(By.ID, 'search-icon-legacy').click()
    time.sleep(2)

    def click_on_vid(elements):
        for i in elements:
            try:
                i.click()
                break
            except:
                continue

    click_on_vid(wd.find_elements(By.ID, 'video-title'))
    print('Video Found')


search_video(wd, Title)
