import logging
def getMyLog():
    # 屏幕显示输出log
    pr = logging.StreamHandler()
    # 将log输出至文件
    file = logging.FileHandler('runLog.log')

    #配置Log
    logging.basicConfig(level=logging.DEBUG,handlers=[pr,file],
                        format="%(asctime)s,%(name)s,%(levelname)s : %(message)s"
                               "-----modelName=%(filename)s,funcName=%(funcName)s,codeLine=%(lineno)s ")
