from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from multiprocessing import Process
from schedule import every, run_pending
from time import sleep

options = Options()
options.profile = '/home/logbaby/.mozilla/firefox/9qna7omd.default-release'
DRIVER = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), firefox_binary=FirefoxBinary(),
                           options=options)

LINK_TO_POST = 'https://vk.com/logbaby?w=wall520436062_2422%2Fall'
VIEWS_COUNT = 1250


def create_boostlike_task(service_link='https://boost-like.ru/vk/besplatnaya-nakrutka-prosmotrov-v-vk/',
                          link=LINK_TO_POST):  # boost-like.ru
    DRIVER.get(service_link)
    main_section = DRIVER.find_element(By.CLASS_NAME, 'main_section')
    field_link = main_section.find_element(By.CLASS_NAME, 'field-link')

    def manage_link():
        if field_link.is_enabled():
            print('[Boost like log] - Button enabled')

            field_link.send_keys(link)
            button_send_views = main_section.find_element(By.CLASS_NAME, 'free-btn')
            button_send_views.click()

            sleep(1)
            DRIVER.minimize_window()

        else:
            print('[Boost like log] - Button disabled')

    manage_link()
    every(15).minutes.do(manage_link)

    while True:
        run_pending()
        sleep(1)


def create_vk_views_task(service_link='https://lk.vkviews.ru/task/add/post'):  # vkviews.ru
    DRIVER.get(service_link)
    input_icon_block = DRIVER.find_element(By.CLASS_NAME, 'input_icon_block')
    input_icon_block.find_element(By.CLASS_NAME, 'input').send_keys(LINK_TO_POST)

    input_digits_block = DRIVER.find_element(By.CLASS_NAME, 'custom_number_mini ')
    input_digits_block.find_element(By.CLASS_NAME, 'input').clear()
    input_digits_block.find_element(By.CLASS_NAME, 'input').send_keys(VIEWS_COUNT)

    try:
        DRIVER.find_element(By.CLASS_NAME, 'btn_icon').click()
    except Exception:
        print('[Vk views log] - Button blocked')

    sleep(5)


if __name__ == '__main__':
    create_vk_views_task()
    Process(target=create_boostlike_task, args=('https://boost-like.ru/vk/besplatnaya-nakrutka-prosmotrov-v-vk/',
                                                'https://vk.com/logbaby?w=wall520436062_2431%2Fall')).run()
