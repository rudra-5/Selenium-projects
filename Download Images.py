import io
import os
import time
import timer
from threading import Timer
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

Name = input("Enter the name of the pic: ")
Num_of_pics = int(input("Number of Images: "))

PATH = 'C:\\Users\\Lenovo\\Desktop\\Progamming\\WebScrapping\\chromedriver.exe'
wd = webdriver.Chrome(PATH)
wd.maximize_window()
wd.implicitly_wait(20)


def get_images(web_driver, delay, max_images, url):
    def scroll_down(web_driver):
        web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(delay)

    web_driver.get(url)

    image_url_set = set()
    skips = 0
    scroll_down(web_driver)
    while len(image_url_set) + skips < max_images:

        thumbnail_url = web_driver.find_elements(By.CLASS_NAME, 'Q4LuWd')

        for img in thumbnail_url[len(image_url_set) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            images = web_driver.find_elements(By.CLASS_NAME, 'n3VNCb')

            for image in images:
                if image.get_attribute('src') in image_url_set:
                    max_images += 1
                    skips += 1
                    break
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_url_set.add(image.get_attribute('src'))
                    print(f'Found image {len(image_url_set)}')

    return image_url_set


def download_images(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name
        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG')
        print('success')
    except Exception as e:
        print('Failed - ', e)


Search_term = '+'.join(Name.split())
Collected_images = get_images(wd, 2, Num_of_pics,
                              f'https://www.google.com/search?q={Search_term}'
                              f'&tbm=isch&ved=2ahUKEwjTn5Cagu30AhWH_4UKHfksDl0Q2-cCegQIABAA&oq={Search_term}&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6BAgAEENQiOcJWIjnCWCg6QloAnAAeACAAZQCiAHWBJIBBTAuMi4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Yae9YZPrEIf_lwT52bjoBQ&bih=581&biw=1280')
wd.quit()
print('-' * 30)
os.mkdir(f'.\\{Name}\\')


def move_on():
    global a
    a = False



for i, collectedImage in enumerate(Collected_images):
    t = Timer(10, move_on)
    a = True
    t.start()

    if a:
        download_images(f'.\\{Name}\\', collectedImage,
                        Name + '_' + str(i) + '.jpg')
        if not a:
            continue
    t.cancel()