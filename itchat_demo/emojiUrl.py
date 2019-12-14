import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


def getEmoji(username,imagePath):
    # img_path = r'D:\gitSources\itchat_demo\emoji_picture\tx.jpg'
    # f = open(path, 'rb')
    # url = 'http://ericandrewlewis.github.io/emoji-mosaic/?ref=producthunt'
    chromeDriverPath = r'C:\Program Files\Python35\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
    url = 'http://localhost:8000/'
    option = Options()
    path1 = r'D:\gitSources\itchat_demo\emoji_image'
    directory_path = os.path.join(path1,username)
    prefs = {
        'profile.default_content_settings.popups': 0,
        'download.default_directory': directory_path,
    }
    option.add_experimental_option('prefs', prefs)
    option.add_argument("--no-sandbox")
    option.add_argument("--headless")
    # option.add_argument("--start-maximized")
    option.add_argument('--window-size=1920,1080')
    # r = requests.get(url)
    # print(r)
    # res = r.content
    # print(res)
    driver = webdriver.Chrome(chrome_options=option,executable_path=chromeDriverPath)
    driver.get(url)
    up_load = driver.find_element_by_id('loadImage')
    up_load.send_keys(imagePath)
    time.sleep(10)
    driver.find_element_by_id('downloadImage').click()
    time.sleep(1)
    driver.quit()


# if __name__ == '__main__':
#     getEmoji('tx', r'D:\gitSources\itchat_demo\emoji_picture\tx.jpg')
