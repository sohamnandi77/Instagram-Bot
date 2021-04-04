from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import os
from selenium.common.exceptions import NoSuchElementException


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path=os.path.abspath('chromedriver.exe'))

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        # login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # login_button.click()
        # time.sleep(2)
        user_name_elem = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath(
            "//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def fetch_list(self, post_url):
        driver = self.driver
        time.sleep(2)
        driver.get(post_url)
        time.sleep(2)
        number_of_likes = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[2]/div/div[2]/button/span').text
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[2]/div/div[2]/button').click()
        i = 1
        # for i in range(1,int(number_of_likes)+1):
        # self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[{}]'.format(i))
        try:
            check_follow = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/div/div/div[1]/div[3]/button')
            # print(check_follow)
            # print(type(check_follow))
            if check_follow.text == 'Follow':
                user = self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/a/div/div/div').text
                with open(os.path.join(sys.path[0], "potentional_list.txt"), "a", encoding="utf-8") as g:
                    g.write(user)
                    g.write('\n')
        except NoSuchElementException:
            followers_panel = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/div')
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", followers_panel)


if __name__ == "__main__":

    username = ""  # * Enter Your Username
    password = ""  # * Enter Your Password

    ig = InstagramBot(username, password)
    ig.login()

    post_url = ''  # Enter Post Url

    ig.fetch_list(post_url)
