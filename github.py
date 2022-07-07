from githubuserinfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome(r"C:\Users\Admin\Desktop\python_temelleri\selenyum\chromedriver.exe")
        #username and password is importing from githubuserinfo.py file
        self.username = username
        self.password = password
    def singin(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys(self.username)
        password = self.browser.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()

github = GitHub(username, password)
github.singin()
