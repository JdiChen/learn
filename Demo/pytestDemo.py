import pytest
from selenium import webdriver
import os
# def setup():
#     print('setup')
# def teardown():
#     print('teardown')
# def test_6():
#     print('test_6')
#     assert 3 == 3
# def test_7():
#     print('test_7')
#     assert 5==5
# def test_5():
#     print('test_5')
#     assert 6==6
class TestCase():
    # def setup_class(self):
    #     print('setup')
    #
    # def teardown_class(self):
    #     print('teardown')
    def test_1(self,login):
        print('test_1')
        assert 3 == 3

    def test_2(self):
        print('test_2')
        assert 5 == 5

    def test_3(self):
        print('test_3')
        assert 8 == 7

if __name__=='__main__':
    # os.system('pytest -s pytestDemo.py --html=./report/report.html --rerun 3')
    # #pytest.main(['-s','--html=./report/report.html','pytestDemo.py','-rerun 3'])
    pytest.main(['-s','pytestDemo.py','-m=web'])