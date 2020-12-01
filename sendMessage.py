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

contact = "Again"
contact_reduced = "Again"

#contact = "Celia bb 🦚❤️"
#contact_reduced = "Celia bb"
text = "Mensaje de pruebas"
time.sleep(20)

find_user = '//*[@id="side"]/div[1]/div/label/div'
find_user_box = (driver.find_element_by_xpath(find_user)).click()
#find_user_box.send_keys(contact_reduced)
find_user_text = '//*[@id="side"]/div[1]/div/label/div/div[2]'
#find_user_textbox = (driver.find_element_by_xpath(find_user_text)).send_keys(contact_reduced)
a = driver.find_element_by_xpath(find_user_text)
a.clear()
a.send_keys(contact_reduced)
time.sleep(3)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact))
user.click()

time.sleep(5)
#msg_box = driver.find_element_by_class_name('DuUXI')
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msg_box.send_keys(text)

time.sleep(2)

button_send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
button_send.click()

##########################################################################
time.sleep(2)

all_message = '//*[@id="main"]/div[3]/div/div/div[3]/div[20]'
i=1

try:
  while 1 < 2:
    all_message = '//*[@id="main"]/div[3]/div/div/div[3]'
    all_message = all_message+"/div["+str(i)+"]"
    message_pool = (driver.find_element_by_xpath(all_message))
    print("Numero: "+str(i))
    i=i+1
        
except:
  print("An exception occurred")

print("Seguimos con la ejecucion: "+str(i))
i = i-1

last_message = '//*[@id="main"]/div[3]/div/div/div[3]/div['+str(i)+']/div/div/div/div[1]/div/span[1]/span'
last_message_text = (driver.find_element_by_xpath(last_message))
print(str(last_message_text.text()))

#message_pool = (driver.find_element_by_xpath(all_message))
#print(len(message_pool))

