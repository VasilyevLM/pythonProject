import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome()
browser.get('https://gk-mact.ru')

title = browser.title
print(title)
# coockie = browser.find_element(By.XPATH, '/html/body/div[8]/div/div/div[3]/span[1]').click()
submit = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/form/div[3]/div/button')
browser.execute_script('arguments[0].scrollIntoView();', submit)
# browser.execute_script("window.scrollTo(5, 2500)")
time.sleep(5)

text_box = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/form/div[2]/div[1]/div[1]/input')
text_box2 = browser.find_element(By.XPATH, '/html/body/div[4]/div[6]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/form/div[2]/div[1]/div[2]/input')

text_box.send_keys('Test')
text_box2.send_keys('9201337011')
time.sleep(3)

submit.click()

time.sleep(3)
browser.close()
browser.quit()


# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#
# elements = browser.find_element('btn btn-default white has-ripple').click()


# assert 'btn btn-default animate-load has-ripple' in browser.
#
# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()
