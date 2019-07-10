from appium import webdriver
import os
class Father(webdriver.webdriver.WebDriver):
    def __init__(self):
        print('father init')
    def test(self):
        print('father test')

if __name__=='__main__':
    t = Father()
    t.get_screenshot_as_file()
    t.get_screenshot_as_png()
    t.test()

s = webdriver.Remote()
s._switch_to.context()