def testDecorator(func):
    def innner(n): #一定需要内层函数，否则会造成未调用即运行函数
        print('装饰器内部')
        ret = func(n)
        return ret
    return innner

@testDecorator
def test(x):
    print(x+5)
test(10)
