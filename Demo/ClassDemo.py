# class ClassDemo:
#     a=''
#     b=''
#     c=''
#     def test(self,a,b=None,c=None):
#         self.a=a
#         self.b=b
#         self.c=c
#     def show(self):
#         print(self.a,self.b,self.c)
#
# if __name__=='__main__':
#     s = ClassDemo()
#     # b = ClassDemo(12,'ad')
#
#     #print(s.test())
#     print(s.show())
#     s.test(12)
#     print(s.show())
#     s.test(146,31)
#     print(s.show())
import bisect


val = [56,54,97,31,54,12,879,53,458,12,54,3,1]

result = []
for i in val:
    pos = bisect.bisect(result,i)

    bisect.insort(result,i)
    print('{:4}   {:4}'.format(i,pos),result)
