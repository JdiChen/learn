def do_puls(x,y):
   # try:
        if x.isdigit() and y.isdigit():#type(float(x)) == float and type(float(x)) == float:
            x=float(x);y=float(y);
            return x+y
        elif (x.isalpha() and y.isalpha()):#type(x) == str and type(y) == str):
            return x + y
        else:
            return "请两个数字或者字符"
 #   except:
  #          return "请两个数字或者字符"
def testParameter(*value):
    print(value)
if __name__=="__main__":
    # testParameter(a=1,b=2,c=2,d=3,f=4)
    testParameter(1,2,3)

