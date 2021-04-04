from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import os

# * Messaging a particular set of poeple


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
        self.driver = webdriver.Chrome(
            executable_path=os.path.abspath('chromedriver.exe'))

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)
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
        time.sleep(3)
        driver.get('https://www.instagram.com/')
        # driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]    ').click()

    def like_photo(self, user):
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.instagram.com/" + user + "/")
        time.sleep(2)

        # * Write your messages
        message1 = u'you have an Amazing feed \u2764'
        message2 = u'Check out my profile too'
        message3 = 'follow for follow'
        # follow the user
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
            time.sleep(3)
            # message button
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button').click()
            time.sleep(2)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
            time.sleep(1)
            # driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
            # time.sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message2)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message3)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button').click()
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/button').click()
            # gathering photos
            driver.get("https://www.instagram.com/" + user + "/")
            time.sleep(2)
            pic_hrefs = []
            try:
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href)
                 for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except:
                pass
            # Liking photos
            i = 0
            while(i < 10):
                for pic_href in pic_hrefs[:11]:
                    driver.get(pic_href)
                    time.sleep(2)
                    heart = driver.find_element_by_xpath(
                        '//*[@class="_8-yf5 "]').get_attribute('aria-label')
                    if heart == 'Like':
                        try:
                            # time.sleep(2)
                            like = driver.find_element_by_xpath(
                                '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button')
                            like.click()
                            time.sleep(2)
                            i += 1
                        except Exception as e:
                            time.sleep(2)
                    else:
                        i += 1
                        continue
            delete_line(user)

        except:
            pass


if __name__ == "__main__":

    username = ""  # * Enter your Username
    password = ""  # * Enter your Password

    ig = InstagramBot(username, password)
    ig.login()

    user = [line.rstrip('\n') for line in open(
        os.path.join(sys.path[0], "potentional_list.txt"))]

    for i in user:
        ig.like_photo(i)
