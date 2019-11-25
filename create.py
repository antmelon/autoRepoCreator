import sys
import os
from selenium import webdriver

path = "your code directory"
browser = webdriver.Chrome()
browser.get('https://github.com/login')


def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys('your github username')
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys('your github password')
    python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[8]")[0]
    python_button.click()
    browser.get('https:/github.com/new')
    python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    python_button.send_keys(folderName)
    python_button = browser.find_elements_by_css_selector('button.first-in-line')[0]
    python_button.submit()


if __name__ == "__main__":
    create()