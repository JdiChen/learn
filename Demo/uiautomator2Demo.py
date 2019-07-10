import uiautomator2 as u2
import time
d = u2.connect_usb()
# d.app_clear('com.netease.cloudmusic')
# d.disable_popups()
# d.app_start('com.netease.cloudmusic')
# time.sleep(10)
tip = "当前网络不可用，请检查你的网络设置"
d.xpath('//android.widget.TextView[@text="本地音乐"]').click()
# i=0
# for e in d.xpath('//android.widget.TextView[@text="本地音乐"]').all():
#
#     print(e.text+" "+str(i))
#     i+=1
toast = d.toast.get_message(5.0,10.0,'no toast')
print('toast is '+toast)
assert tip==toast
d.close()