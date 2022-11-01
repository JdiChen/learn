import requests

# 第一次封装
# 第二次封闭导入baseapi
from Demo.test.BaseApi import BaseApi


class ApiObject(BaseApi):
    host = 'http://127.0.0.1:5000'

    def add_user(self, body):
        path = "/addUser"
        # r = requests.post(self.host + path, json=body)
        req = {
            "method": "POST",
            "url": self.host + path,
            "json": body
        }
        return self.send_req(req)

    def find_user(self, body):
        name = body["user_name"]
        path = f"/findUser/{name}"
        # r = requests.get(self.host + path)
        req = {
            "method": "GET",
            "url": self.host + path

        }
        return self.send_req(req)

    def del_user(self, body):
        path = "/delUser"
        # r = requests.post(self.host + path, json=body)
        req = {
            "method": "POST",
            "url": self.host + path,
            "json": body
        }
        return self.send_req(req)
