
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome()
browser.get('https://gk-mact.ru')

title = browser.title
print(title)

browser.implicitly_wait(0.5)

text_box = browser.find_element(By.CLASS_NAME, 'inputtext')
text_box2 = browser.find_element(By.CLASS_NAME, 'phone')

text_box.send_keys('Test')
text_box2.send_keys('9201337011')
submit = browser.find_element(By.CLASS_NAME, 'btn btn-default has-ripple')
submit.click()

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
