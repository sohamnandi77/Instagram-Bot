from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot():
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            'prefs', {'intl.accept_languages': 'en,en_US'})
        # self.browser = webdriver.Chrome('./chromedriver_win32/chromedriver/chromedriver.exe', chrome_options=self.browserProfile)
        self.browser = webdriver.Chrome("./chromedriver_win32/chromedriver")
        self.email = ''  # Enter username
        self.password = ''  # Enter password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = browser.find_elements_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        passwordInput = browser.find_elements_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")

    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath(
                '//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")

    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector(
            'div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(
            followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(
                followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector(
                'a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers

    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()


if __name__ == "__main__":

    ig = InstagramBot()
    ig.signIn()
    # * Edit the username and number of followers
    ig.getUserFollowers('petermckinnon', 100)
