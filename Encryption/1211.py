import requests

global token
def getTokem():
    url = "http://admin-api2.tctest5.com/admin/login"
    data = {"username": "admin", "password": "123456", "code": "1240", "token": "5b7b3102b334ac844b524f91b9af176b"}
    headers = {'Platform-Code': 'merchantManage'}
    response = requests.post(url=url, data=data, headers=headers)
    global token # 告诉编译器我在这个方法中使用的token是刚才定义的全局变量token,而不是方法内部的局部变量.
    token = response.json().get('data').get('token')
    #return token


def ref():
   global token # 同样告诉编译器我在这个方法中使用的token是刚才定义的全局变量token,并返回全局变量token,而不是方法内部的局部变量.
   print(token)

if __name__ == '__main__':
    getTokem()
    ref()