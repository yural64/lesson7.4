from selenium import webdriver
#Модуль для работы со временем
import time

browser = webdriver.Chrome()
#Сайт для подключения
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#Делаем скрин и сохраняем в файл dom.png
browser.save_screenshot("dom.png")
#На какое время подключаемся (10 сек)
time.sleep(10)
#Открываем другую страницу
browser.get("https://en.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(10)
#Отключаемся
browser.quit()