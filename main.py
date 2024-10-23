from selenium import webdriver
#Модуль для работы со временем
import time

browser = webdriver.Chrome()
#Сайт для подключения
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#На какое время подключаемся (10 сек)
time.sleep(10)
#Открываем другую страницу
browser.get("https://en.wikipedia.org/wiki/Selenium")
time.sleep(10)
#Отключаемся
browser.quit()