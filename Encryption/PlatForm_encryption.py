import unittest
import requests
import time

import HTMLTestReportCN
class PlatForm_encryption(unittest.TestCase):

#Autotest

    def setUp(self):
        self.main_url = "http://play-api.tctest0.com"#环境切换
        login_url = self.main_url+"/manager/1.0/login"
        login_data = {"account":"wz","password":"e10adc3949ba59abbe56e057f20f883e"}
        login_headers = {'Platform-Code': 'application/x-www-form-urlencoded'}
        login_response = requests.post(url=login_url, data=login_data, headers=login_headers)
        # print(login_response.status_code)
        #print(login_response.text)
        self.token = login_response.json().get('data').get('token')


    def test_login(self):
        #z登录
        login_movietype_url = self.main_url+"/movietype/1.0/list?pageNum=1&pageSize=999"
        login_movietype_headers = {'token':self.token}
        login_movietype_respones = requests.get(url=login_movietype_url,headers = login_movietype_headers)
        #print(login_movietype_url_respones.json().get('meg'))
        #print(login_movietype_respones.json())
        #print(login_movietype_respones.status_code)
        self.assertEqual(login_movietype_respones.status_code, 200)
        self.assertEqual(login_movietype_respones.json().get('msg'),'成功')

        login_queryMovieList_url = self.main_url+"/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        login_queryMovieList_headers = {'token':self.token}
        login_queryMovieList_respones = requests.get(url=login_queryMovieList_url,headers = login_queryMovieList_headers)
        #print(login_queryMovieList_url_respones.json().get('meg'))
        #print(login_queryMovieList_respones.json())
        #print(login_queryMovieList_respones.status_code)
        self.assertEqual(login_queryMovieList_respones.status_code, 200)
        self.assertEqual(login_queryMovieList_respones.json().get('msg'),'成功')

    def test_queryMovieLis(self):
        #高清加密
        movietype_url = self.main_url+"/manager/1.0/queryMovieList?title=Autotest&pageNum=1&pageSize=10&displayType=1"
        movietype_headers = {'token':self.token}
        movietype_respones = requests.get(url=movietype_url,headers = movietype_headers)
        id = int(movietype_respones.json().get('data').get('data')[0].get('id'))
        self.assertEqual(movietype_respones.status_code, 200)
        self.assertEqual(movietype_respones.json().get('msg'),'成功')

        #加密按钮
        encryptFile_url = self.main_url + "/manager/1.0/encryptFile"
        encryptFile_headers = {'token': self.token,'Platform-Code': 'application/x-www-form-urlencoded'}
        encryptFile_data = {"id": id}
        encryptFile_respones = requests.post(url=encryptFile_url, data=encryptFile_data, headers=encryptFile_headers)
        # print(login_encryptFile_url_respones.json().get('meg'))
        print(encryptFile_respones.json())
        # print(login_encryptFile_respones.status_code)
        #self.assertEqual(encryptFile_respones.status_code, 200)
        #self.assertEqual(encryptFile_respones.json().get('msg'), '成功')

        queryMovieListA_url = self.main_url+"/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        queryMovieListA_headers = {'token':self.token}
        queryMovieListA_respones = requests.get(url=queryMovieListA_url,headers = queryMovieListA_headers)
        #print(queryMovieListA_url_respones.json().get('meg'))
        #print(queryMovieListA_respones.json())
        #print(queryMovieListA_respones.status_code)
        self.assertEqual(queryMovieListA_respones.status_code, 200)
        self.assertEqual(queryMovieListA_respones.json().get('msg'),'成功')

        #编辑按钮






    def tearDown(self):
        #print('接口测试通过')
        pass

if __name__ == "__main__":
    unittest.main()