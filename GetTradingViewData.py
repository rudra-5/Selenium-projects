import time
from selenium import webdriver
from selenium.webdriver.common.by import By




PATH = 'C:\\Users\\Lenovo\\Desktop\\Programming\\WebScrapping\\chromedriver.exe'
wd = webdriver.Chrome(PATH)
wd.maximize_window()
wd.implicitly_wait(20)

def get_chart(symbol):
    url = 'https://www.tradingview.com/chart/?symbol='

    url += symbol
    wd.get(url)
    time.sleep(5)
    a = wd.find_element(By.CLASS_NAME, 'chart-markup-table')

    a.screenshot("chart.png")



def get_earnings(symbol):
    url = 'https://www.tradingview.com/chart/?symbol='

    url += symbol
    wd.get(url)
    time.sleep(5)
    key_stats = wd.find_element(By.CLASS_NAME, "wrap-C64bdFhg")
    key_stats.screenshot("Earnings.png")
    date = wd.find_element(By.CLASS_NAME, 'upcomingEarnings-dkwk1RQ0').find_element(By.CLASS_NAME, 'upcomingDate-dkwk1RQ0')
    return date.text

def get_market_sentiments(symbol):
    url = 'https://www.tradingview.com/chart/?symbol='

    url += symbol
    wd.get(url)
    time.sleep(5)
    technicals = wd.find_element(By.CLASS_NAME, 'container-bKC4jg1o')
    technicals.screenshot('technicals.png')

