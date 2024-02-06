from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_yandex(query):
    # Настройка веб-драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Открытие Yandex
        driver.get("https://yandex.ru")

        # Нахождение поля поиска и ввод запроса
        search_box = driver.find_element(By.NAME, "text")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Ожидание загрузки результатов
        time.sleep(5)

        # Извлечение ссылок из результатов поиска
        search_results = driver.find_elements(By.XPATH, '//a[@href]')
        urls = [result.get_attribute('href') for result in search_results]

        return urls

    finally:
        driver.quit()

# Пример использования
query = "пример запроса"
urls = search_yandex(query)
for url in urls:
    print(url)
