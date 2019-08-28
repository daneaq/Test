#Author : Danea
import unittest
import requests


def setUpModel(self):
    print("----setUpModel----")


def tearDownModel(self):
    print("----tearDownModel----")

class TestUserLogin(unittest.TestCase):

    url="http://115.28.108.130:5000/api/user/login/"

    def test_uer_login_normal(self):
        data = {"name":"张三","password":"123456"}
        res = requests.post(url=self.url,data=data)
        self.assertIn('登录成功',res.text)

    def test_user_login_wrong(self):
        data = {'name':'张三','password':'1234567'}
        res = requests.post(url=self.url,data=data)
        self.assertIn('失败',res.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)