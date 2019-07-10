from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()#最大化窗口
        self.driver.implicitly_wait(10)#设置隐式等待

    # def testLogin(self):
    #     #     # self.driver.get("http://eip.longcheer.com")
    #     #     self.driver.get('http://jira.longcheer.net:8080/issues/?filter=-4')
    #     #     print(self.driver.title)
    #     #     s = WebDriverWait(self.driver,10).until(expected_conditions.title_is('[所有问题] 问题导航栏 - LongCheer JIRA'),'无法打开网页')
    #     #     print(s)
    #     #     self.driver.find_elements_by_tag_name('div')
    #     #     self.driver.find_element_by_id('txtUserName').send_keys('chenqiang')
    #     #     self.driver.find_element_by_id('txtPassword').send_keys('Chen0123')
    #     #     self.driver.find_element_by_id('btnLogin').click()
    #     #     e = self.driver.find_element_by_id('linkLogOff')
    #     #     s = e.get_attribute('text')
    #     #     print(s)
    #     #     self.assertIn('退出登录',s)#验证登录是否成功，反馈给测试结果，不成功刚测试结果为失败
    #     #     e.click()
    #     #     time.sleep(5)
    def testSelect(self):
        d = self.driver
        d.get('http://172.17.160.220:8088/bug/')
        print(type(WebDriverWait(d,10).until(lambda x:x.find_element_by_xpath('//*[@id="fre"]'),'无法找到元素')))
        se = Select(d.find_element_by_xpath('//*[@id="fre"]'))
        print(se.options)
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__=='__main__':
    #第一种方法
    #unittest.main() 加载全部用例
    #第二种方法
    tests = unittest.TestLoader().loadTestsFromTestCase(SeleniumTest) #实例化测试用例类
    suite = unittest.TestSuite(tests) #测试用例加载至测试套件
    unittest.TextTestRunner().run(suite) #运行测试结果
