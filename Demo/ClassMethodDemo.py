class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @classmethod
    def show(cls):
        print(123)
        print(456)
s = test(4,5)
s.show()
test.show()