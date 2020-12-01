from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from keyboard import press


#driver = webdriver.Chrome(executable_path=r'C:/Users/MS-DIEZ/Desktop/chromedriver_win32/chromedriver.exe')
options = webdriver.ChromeOptions();
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path=r'C:/Users/MS-DIEZ/Desktop/chromedriver_win32/chromedriver.exe', chrome_options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')
time.sleep(20)

all_message = '//*[@id="main"]/div[3]/div/div/div[3]'
message_pool = (driver.find_element_by_xpath(all_message)).click()
print(message_pool)