import time
#以字符串形式返回当前时间，eg:Wed Jul 10 11:43:16 2019
asctime = time.asctime()
print('asctime = ',asctime)
#time.clock()已弃用,返回从线程开始运行到此处的时间
clock = time.process_time()
print('clock = ',clock)
#ctime()参数可传秒数，计算自Epoch以来到参数秒数的时间，不传刚返回当前时间
ctime = time.ctime()
print('ctime = ',ctime)
#返回传入当前时间参数的time.struct_time类
gmtime = time.gmtime()
print('gmtime = ',gmtime)
localtime = time.localtime()
print('localtime = ',localtime)
#将当前时间的元组转换为至纪元以来的秒数
mktime = time.mktime(localtime)
print('mktime = ',mktime)
#单调时钟，不能回退，ns为精确到纳秒
Mclock = time.monotonic()
print('Mclock = ',Mclock)
MclockNs = time.monotonic_ns()
print('MclockNs = ',MclockNs)
#性能计数器,返回程序运行至此的时间,ns为精确到纳秒
perf_counter = time.perf_counter()
print('perf_counter  = ',perf_counter)
#格式化输出时间，参数传入格式化字符串，及时间元组
fromatstr = '%Y%m%d%H%M%S'
strftime = time.strftime(fromatstr,localtime)
print('strftime = ',strftime)
#将格式化输出的时间，格式化成时间元组
strptime = time.strptime(strftime,fromatstr)
print('strptime = ',strptime)
#返回纪元以来至当前时间的秒数
mytime = time.time()
print('time = ',mytime)
