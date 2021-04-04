from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import os


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


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

    def like_photo(self, post_link):
        driver = self.driver
        time.sleep(2)
        driver.get(post_link)
        time.sleep(2)
        while True:
            driver.get(post_link)
            time.sleep(2)
            comment = driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
            comment.click()
            mention = '@'+followers[0]+' '+'@' + \
                followers[1]+' '+'@'+followers[2]+' '
            # comment_text = str(random.choice(comments))
            # comments.remove(comment_text)
            try:
                comment.send_keys(mention)
                post = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button')
                post.click()
                time.sleep(2)
            except:
                comment = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
                comment.send_keys(mention)
                post = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button')
                post.click()
            del followers[0:3]
            time.sleep(random.randint(25, 35))


if __name__ == "__main__":

    username = ""  # * Enter your Username
    password = ""  # * Enter your Password
    post_link = ""  # *  Enter the post link you want ot comment down

    ig = InstagramBot(username, password)
    ig.login()

    # * Do make a file named "followers.txt" to mention their name in the giveaways
    followers = [line.rstrip('\n') for line in open(
        os.path.join(sys.path[0], "followers.txt"))]
    ig.like_photo(post_link)
