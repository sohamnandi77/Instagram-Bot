from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import os

# * Script to DM your followers in the General Section


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


def delete_line(user):
    with open(os.path.join(sys.path[0], "potentional_list.txt"), "r+") as f:
        lines = f.readlines()
        f.seek(0)
        # to erase all data
        f.truncate()
        for line in lines:
            if line.strip("\n") != user:
                f.write(line)


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver_win32/chromedriver")

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)
        user_name_elem = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath(
            "//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get('https://www.instagram.com/')
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]').click()

    def like_photo(self):
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.instagram.com/direct/inbox/general/")
        time.sleep(2)
        message1 = ""  # * Enter your Message you want ot send
        i = 1
        while True:
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{}]/a'.format(i)).click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            time.sleep(1)
            i += 1


if __name__ == "__main__":

    username = ""  # * Enter your username
    password = ""  # * Enter your password

    ig = InstagramBot(username, password)
    ig.login()
    ig.like_photo()
