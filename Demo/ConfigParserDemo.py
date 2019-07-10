import configparser
import os
config = configparser.ConfigParser()
def connect(path):
    d = {}
    config.read(os.path.join('e:','IML','test.txt'))
    for s in config.items('config'):
        d[s[0]] = s[1]
    print(d)
# print(config.items('config'))
# print(config.options('config'))
# print(config.get('config3','test'))
# number = config.getfloat('config','number')
# time = config.getint('config','time',fallback='no time section')
# print(time,type(time))
# config.add_section('mod')
# config.set('mod','modtest','intest')
# fp = open(r'e:\text.ini','w')
# config.write(fp)
