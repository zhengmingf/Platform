import unittest
import requests
import Token


class PlatForm_encryption(unittest.TestCase):
    token = Token.Token.token()





    def setUp(self):
        self.main_url = "http://play-api.tctest0.com"#环境切换
        print(self.token+'1')
    #
    def test_aogin(self):
        #登录
        print(self.token+'2')

        login_movietype_url = self.main_url+"/movietype/1.0/list?pageNum=1&pageSize=999"
        login_movietype_headers = {'token':self.token}
        login_movietype_respones = requests.get(url=login_movietype_url,headers = login_movietype_headers)

        self.assertEqual(login_movietype_respones.status_code, 200)
        self.assertEqual(login_movietype_respones.json().get('msg'),'成功')

        login_queryMovieList_url = self.main_url+"/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        login_queryMovieList_headers = {'token':self.token}
        login_queryMovieList_respones = requests.get(url=login_queryMovieList_url,headers = login_queryMovieList_headers)
        self.assertEqual(login_queryMovieList_respones.status_code, 200)
        self.assertEqual(login_queryMovieList_respones.json().get('msg'),'成功')
        print('高清影片后台登录成功')

        print(self.token+'3')


    def test_FilmEncryption(self):
        #高清加密菜单
        #查询
        movietype_url = self.main_url+"/manager/1.0/queryMovieList?title=Aototest&pageNum=1&pageSize=10&displayType=1"
        print(self.token+'4')



if __name__ == "__main__":
    unittest.main()