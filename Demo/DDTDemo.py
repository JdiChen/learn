from selenium import webdriver
import unittest
from ddt import *
from Demo.loginTest import *
import xlrd
import time
import logging

def getDate(filename):
    rows = []
    f = xlrd.open_workbook(filename)
    table = f.sheet_by_index(0)
    for row in range(1,table.nrows):
        rows.append(table.row_values(row))
    logging.info('getdata pass')
    return rows

@ddt #使用此装饰测试用例才能使用数据驱动测试
class ddtTest(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     d = self.driver
    #     d.get('http://eip.longcheer.com:29002/login.aspx?appcode=1003&returnurl=http%3a%2f%2feip.longcheer.com')
    #     d.implicitly_wait(5)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        logging.info('get server pass')
        d = cls.driver
        d.get('http://eip.longcheer.com:29002/login.aspx?appcode=1003&returnurl=http%3a%2f%2feip.longcheer.com')
        logging.info('get url pass')
        d.implicitly_wait(5)
    @data(*getDate(r'E:\IML\longData.xlsx')) #取得数据
    @unpack #解析数据
    def testLogin(self,user,ps,eql): #将解析到的数据传递给测试用例
        lg = login(self.driver)
        lg.submit(user,ps) #登录操作
        #取得出错提示
        e = self.driver.find_element_by_xpath\
            ('//*[@id="loginForm"]/div[3]/div[2]/div[4]/div').text
        self.assertEqual(eql,e)#断言
        time.sleep(2)
        lg.cls()

    # def tearDown(self):
    #     self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('quit sucessful')

if __name__=='__main__':
    #第一种方法
    #unittest.main() 加载全部用例
    #第二种方法
    tests = unittest.TestLoader().loadTestsFromTestCase(ddtTest) #实例化测试用例类
    suite = unittest.TestSuite(tests) #测试用例加载至测试套件
    logging.info('load suite pass')
    unittest.TextTestRunner().run(suite) #运行测试结果

