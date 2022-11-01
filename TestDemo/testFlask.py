import pytest
import requests

from Demo.test.ApiObject import ApiObject


class TestFlask:

    def setup_class(self):
        self.aob = ApiObject()

    def test_add_user(self):
        # host = "http://127.0.0.1:5000"
        # path = "/addUser"
        body = {
            "user_name": "testadd",
            "age": "28",
            "phone": "123"
        }
        assert "testadd" == self.aob.add_user(body).json()["return_obj"]["user_name"]

    def test_del_user(self):
        # host = "http://127.0.0.1:5000"
        # path = "/delUser"
        body = {
            "user_name": "testdel",
            "age": "28",
        }
        # r = requests.post(host + path, json=body)
        assert "success del testdel done" ==  self.aob.del_user(body).json()["message"]

    def test_find_user(self):
        # host = "http://127.0.0.1:5000"
        name = "testfind"
        # 添加用户查询
        # addPath = "/addUser"
        body = {
            "user_name": name,
            "age": "28",
            "phone": "123"
        }
        # add_r = requests.post(host + addPath, json=body)
        assert name == self.aob.add_user(body).json()["return_obj"]["user_name"]

        # path = f"/userInfo/{name}"
        # r = requests.get(host + path)
        assert name == self.aob.find_user(body).json()["return_obj"]["user_name"]


if __name__ == '__main__':
    pytest.main(["-v"])
