from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.profile = '/home/logbaby/.mozilla/firefox/9qna7omd.default-release'
DRIVER = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), firefox_binary=FirefoxBinary(),
                           options=options)

LINK_TO_POST = 'https://vk.com/logbaby?w=wall520436062_2422%2Fall'
ADD_TO_POST_LINK_VK_VIEWS = 'https://lk.vkviews.ru/task/add/post'
VIEWS_COUNT = 1250

def create_task():
    DRIVER.get(ADD_TO_POST_LINK_VK_VIEWS)
    input_icon_block = DRIVER.find_element(By.CLASS_NAME, 'input_icon_block')
    input_icon_block.find_element(By.CLASS_NAME, 'input').send_keys(LINK_TO_POST)

    input_digits_block = DRIVER.find_element(By.CLASS_NAME, 'custom_number_mini ')
    input_digits_block.find_element(By.CLASS_NAME, 'input').clear()
    input_digits_block.find_element(By.CLASS_NAME, 'input').send_keys(VIEWS_COUNT)

    DRIVER.find_element(By.CLASS_NAME, 'btn_icon').click()

if __name__ == '__main__':
    create_task()
