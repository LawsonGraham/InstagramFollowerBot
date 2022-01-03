from selenium import webdriver
import os
import time
import random
from selenium.webdriver.common.keys import Keys

user_to_find = 'ACCOUNT YOU WANT TO TAKE USERS FROM'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

class InstagramBot:
    def __init__(self, username, password):
        """
        Initialize an instance of the Instagram Bot and logs into Instagram

        Args:
        username: str: The Instagram username for user
        password: str: The Instagram password for user

        Attributes:
        driver: Selenium.webdriver.Chrome: The webdriver that automates browser actions

        """
    
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.arbitrary_user = 'tonyrobbins'
        self.driver = webdriver.Chrome()

        self.login()

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        
        time.sleep(2)

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base_url, user))


    def follow_user(self, user):
        ig_bot.nav_user(user)
        time.sleep(1)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]

        follow_button.click()
        print('followed')
        
    def unfollow_user(self, user):
        try:
            unfollow_button = self.driver.find_elements_by_class_name('_5f5mN ')[0]
        
        except:
            unfollow_button = self.driver.find_elements_by_class_name('sqdOP ')[1]

        unfollow_button.click()
        time.sleep(1)

        unfollow_confirm_button = self.driver.find_elements_by_class_name('aOOlW')[0]

        unfollow_confirm_button.click()
        print('unfollowed')

    def steal_users_followers(self, user):
        ig_bot.nav_user(user)
        time.sleep(2)
        num_followers = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
        times_looped = int(0)
        followed = int(0)
        scroll_count = int(0)
        while followed != num_followers:
            count = int(0)
            see_followers = self.driver.find_elements_by_class_name('-nal3 ')[1]
            see_followers.click()
            time.sleep(3)
            dialog = self.driver.find_element_by_class_name('isgrP')
            for i in range (0, scroll_count):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
                time.sleep(1)
            while int(count) != 25:
                time.sleep(random.randint(500,1000)/1000)
                for i in range (0,12):
                    follow_button = self.driver.find_elements_by_class_name('sqdOP ')[followed]
                    if follow_button.get_attribute("class") == 'sqdOP  L3NKy   y3zKF     ':
                        follow_button.click()
                        count += 1
                        time.sleep(random.randint(150,1000)/1000)
                    followed += 1
                    if count == 25: 
                        break
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
                scroll_count += 1
            self.driver.quit()
            time.sleep(random.randint(300000,360000)/1000)
            times_looped += 1
            print(times_looped)
            ig_bot.__init__(username, password)
            time.sleep(5)
            ig_bot.nav_user(user)
            time.sleep(5)

            
  
    def unfollow_nonfollowers(self, user):
        times_looped = int(0)
        n_lower = int(1000) 
        n_upper = int(2000)
        unfollowed_ticker = int(0)
        ig_bot.nav_user(user)
        followers_before = self.driver.find_elements_by_class_name('g47SY ')[2].get_attribute("title")
        see_followers = self.driver.find_elements_by_class_name('-nal3 ')[1]
        see_followers.click()
        time.sleep(3)
        dialog = self.driver.find_element_by_class_name('isgrP')
        num_followers = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
        counter = int(0)
        list_of_followers = []
        print(followers_before)
        while counter!= num_followers:
            for i in range (0,12):
                if counter == num_followers:
                    break
                follower = self.driver.find_elements_by_class_name('FPmhX')[counter]
                list_of_followers.append(follower.get_attribute("title"))
                counter += 1
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(random.randint(500,1500)/1000)
        close_popup = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button')
        close_popup.click()
        see_following = self.driver.find_elements_by_class_name('-nal3 ')[2]
        see_following.click()
        num_following = int(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text)
        print (num_following)
        counter = int(0)
        dialog = self.driver.find_element_by_class_name('isgrP')
        time.sleep(random.randint(n_lower,n_upper)/1000)
        while counter != num_following:
            for i in range (12):
                if counter == num_following:
                    break
                followed_person = self.driver.find_elements_by_class_name('FPmhX')[counter]
                if followed_person.get_attribute("title") in list_of_followers:
                    counter += 1
                else:
                    time.sleep(1.5)
                    temp_address = self.driver.find_elements_by_class_name('FPmhX')[counter].get_attribute("title")
                    self.driver.execute_script("window.open('https://instagram.com/{}/');".format(temp_address))
                    time.sleep(random.randint(n_lower,n_upper)/1000)
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    time.sleep(random.randint(n_lower,n_upper)/1000)
                    ig_bot.unfollow_user(user_to_find)
                    time.sleep(random.randint(n_lower,n_upper)/1000)
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    time.sleep((random.randint(n_lower,n_upper)*3)/1000)
                    print(followed_person.get_attribute("title"))
                    print('unfollowed', unfollowed_ticker)
                    counter += 1
                    unfollowed_ticker += 1
                    if unfollowed_ticker == 14:
                        time.sleep(random.randint(600000,760000)/1000)
                        unfollowed_ticker = 0
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(4)
            
    def test(self, user):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
if __name__ == '__main__':

    ig_bot = InstagramBot(username, password)
    time.sleep(3)
    ig_bot.unfollow_nonfollowers(username)
