import codecs
import re
import logging
import os
def L():
# logging.getLogger('test')
# logging.disable(logging.CRITICAL)  禁用日志
    logging.debug('debug mesg')
    logging.info('info mesg')
    logging.warning('wrrang mesg')
    logging.error('E message')
    logging.critical('critical error')

def testRe():
    #手机号码
    test = '1[358][0-9]{9}'
    #固话号码
    t2 = '0[\d]{3}-[\d]{4}[\d]{3,4}'
    #账号,只能以下线或者字母开头
    t3 = '[_a-zA-Z]\w{2,15}'
    #电子邮件
    t4 = '\w{6,15}@\w.com'
    t5 = '\D+'
    while True:
        s=input('输入：')
        try:
            t = re.fullmatch(t5,s)
            if(not t):
                print('规则不正确')
            else:
                print('输入正确'+t.group())
        except Exception as e:
            print(e)

def testReFile():
    fp = codecs.open(r'D:\chenqiang\桌面\乱\GCD\test.txt','r',encoding='utf-8')
    text = fp.read()
    fp.close()
    rst = re.finditer('[a-z][\u4e00-\u9fa5]',text)
    for r in rst:

        print(r.group())


#testReFile()
