import unittest
def t(func):
    def myfunc(tset):
        print(func._outcom.success)
        def inner(self):
            return tset()
        return myfunc

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1,2)
    @unittest.skipIf('test1','skip test_add')
    def test2(self):
        print(self._outcome.success)
        print('test2')
if __name__ == '__main__':
    # suite = unittest.TestSuite()#测试用例集
    # suite.addTest(MyTest('test_add'))#向用例集添加用例项
    # a = unittest.TestResult()#测试结果
    # suite.run(result=a)#输出测试结果
    # print('a='+str(a))
    unittest.main()

