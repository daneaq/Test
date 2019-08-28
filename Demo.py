#Author : Danea

#导入requests包
import requests
import json

#1.URL请求地址
url = "http://httpbin.org/get"
#2.发送请求，获取相应结果
res_body1 = requests.get(url)
#3.解析相应
# print(res_body1.text)

###带参数的GET请求
url = "http://www.tuling123.com/openapi/api"
params ={"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"}
res_body2 = requests.get(url,params)
# print(res_body2.text)


url = "http://httpbin.org/post"
###传统表单类POST请求
data1 = {"name": "hanzhichao", "age": 18}
# res_body3 = requests.post(url=url,data=data)
# print(res_body3.text)

###json类型的POST请求
data2 = '''
    {
    "name":"zhangzhil",
    "age":19
    }
'''
# res4 = requests.post(url=url,data=data2)
# print(res4.text)

data3 = {
    "name":"lisi",
    "age":23
}
headers = {"Content-Type":"application/json"}
# res5 = requests.post(url=url,data=json.dumps(data3),headers=headers)
# print(res5.text)


#http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好
#key=e3afc23717ee45f5976ec03c64fdd32b

# str = input("请输入: ")
url= "http://www.tuling123.com/openapi/api"
params = {"key":"e3afc23717ee45f5976ec03c64fdd32b","info":str}
# res6 = requests.get(url=url,params=params)
# print(res6.text)

def find_food(url,data):
    res = requests.post(url=url,json=data)
    print(res.text)

url = "http://www.tuling123.com/openapi/api"
data = {
    "key":"e3afc23717ee45f5976ec03c64fdd32b",
    "info":"上地华联附近的酒店",
     "loc":"北京市海淀区信息路28号",
    "userid":"123456789"
}
# find_food(url,data)

# s = requests.session() #新建一个会话
# url = "https://demo.fastadmin.net/admin/index/login.html"
# data = {"username":"admin","password":"123456"}
# res8 = s.post(url,data)
# res9 = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs")
# print(res8)
# print(res9.text)

#携带cookie登录
