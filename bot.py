from selenium import webdriver
from time import sleep
from secrets import password


class GitBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            'C:/Users/Utsav/Desktop/Coding/Python/1_bot_git/chromedriver/chromedriver.exe')

    def login(self):
        self.driver.get('https://github.com/login')
        sleep(2)
        email_in = self.driver.find_element_by_id('login_field')
        email_in.send_keys('utsaveshan0206@gmail.com')
        Password = self.driver.find_element_by_id('password')
        Password.send_keys(password)
        sign_in = self.driver.find_element_by_name('commit')
        sign_in.click()

    def create_repo(self):
        print('Hey, I am creating a repository, give me a name for this project')
        repo_name = input()
        repo_btn = self.driver.find_element_by_link_text(
            'New')
        repo_btn.click()
        repo_form = self.driver.find_elements_by_id('repository_name')
        repo_form[0].send_keys(repo_name)
        create_btn = self.driver.find_element_by_class_name('first-in-line')
        sleep(2)
        create_btn.click()
        copy_btn = self.driver.find_element_by_tag_name('clipboard-copy')
        copy_btn.click()


bot = GitBot()
bot.login()
bot.create_repo()
