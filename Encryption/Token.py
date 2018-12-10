import requests

def token():
        #登录
        main_url = "http://play-api.tctest0.com"  # 环境切换
        login_url = main_url+"/manager/1.0/login"
        login_data = {"account":"zdh","password":"e10adc3949ba59abbe56e057f20f883e"}
        login_headers = {'Platform-Code': 'application/x-www-form-urlencoded'}
        login_response = requests.post(url=login_url, data=login_data, headers=login_headers)
        token = login_response.json().get('data').get('token')
        return token