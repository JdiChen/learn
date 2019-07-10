import enum

"""@enum.unique
class test_enum(enum.Enum):
    new = 7
    inc = 6
    inva = 5
    wont = 4
    inp = 3
    fixc = 2
    fixr = 1

    coy = 1
    copy_new = 7"""
def test():
    test_enum = enum.Enum(value='test_enum',
                          names='new inc inva wont inp fixc fixr')
    for test in test_enum:
        print('{}={}'.format(test.name,test.value))
    print(test_enum.inc == test_enum.fixr)
    print(test_enum.new is test_enum.new)


def t2(s):
    s2=''
    for i in range(0,len(s)-1):
        s2 += str(s[i])+','
    print('\n'+s2+'and '+s[-1])
m = [x for x in 'adbcdefg']
t2(m)