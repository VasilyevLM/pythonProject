import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'

browser = webdriver.Chrome(options=options)
browser.get('https://gk-mact.ru')

title = browser.title
print(title)

submit = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/form/div[3]/div/button')
browser.execute_script('arguments[0].scrollIntoView();', submit)

time.sleep(5)

text_box = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/form/div[2]/div[1]/div[1]/input')
text_box2 = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/form/div[2]/div[1]/div[2]/input')

text_box.send_keys('Test')
text_box2.send_keys('9201337011')
time.sleep(1)

submit.click()

time.sleep(1)

time.sleep(1)
browser.execute_script("window.scrollTo(5, 3500)")
time.sleep(3)
product = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[6]/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]')
browser.execute_script('arguments[0].scrollIntoView();', product)
time.sleep(3)
product.click()
time.sleep(3)
browser.execute_script("window.scrollTo(5, 500)")
time.sleep(3)
buy = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/span[1]')
browser.execute_script('arguments[0].scrollIntoView();', buy)
time.sleep(3)
buy.click()
# time.sleep(3)
# basket = browser.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[1]/div[1]/div/div/span')
# basket.click()
time.sleep(3)
basket2 = browser.find_element(By.XPATH, '/html/body/div[7]/div/div/div/form/ul/li/div[1]/div[3]/div[2]/div[1]/a')
basket2.click()
time.sleep(3)
order = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div[1]/button')
order.click()
time.sleep(10)









# browser.close()
# browser.quit()


# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#
# elements = browser.find_element('btn btn-default white has-ripple').click()


# assert 'btn btn-default animate-load has-ripple' in browser.
#
# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()
