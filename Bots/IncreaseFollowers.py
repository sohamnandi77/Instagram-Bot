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

    def like_photo(self, hashtag):
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 3):
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
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs[:50]:
            driver.get(pic_href)
            time.sleep(2)
            heart = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/svg')
            if heart.get_attribute('aria-label') == 'Like':
                # try:
                like = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                like.click()
                comment = driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
                comment.click()
                comment_text = str(random.choice(comments))
                comments.remove(comment_text)
                try:
                    comment.send_keys(comment_text)
                    comment.send_keys(Keys.ENTER)
                    time.sleep(2)
                except:
                    comment = driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
                    comment.send_keys(comment_text)
                    post = driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button')
                    post.click()

                for second in reversed(range(0, random.randint(25, 35))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
                unique_photos -= 1
            else:
                continue


if __name__ == "__main__":

    username = ""  # * Enter your Username
    password = ""  # * Enter your Password

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = [line.rstrip('\n') for line in open(
        os.path.join(sys.path[0], "hashtags.txt"))]

    # * Choose a random tag from the list of tags
    tag = random.choice(hashtags)
    comments = [line.rstrip('\n') for line in open(
        os.path.join(sys.path[0], "messages.txt"))]
    ig.like_photo(tag)
