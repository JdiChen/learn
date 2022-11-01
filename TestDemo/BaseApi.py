# 第二次封装
import requests


class BaseApi:
    def send_req(self, req):
        return requests.request(**req)
