'''
Задание: работа с выпадающим списком
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome(executable_path=r'D:\Download\chromedriver_win32\chromedriver.exe') as browser:
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    answer = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(answer)

    browser.find_element_by_tag_name('button').click()
    time.sleep(10)
