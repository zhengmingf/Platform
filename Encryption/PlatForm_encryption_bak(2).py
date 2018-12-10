import unittest
import requests
class PlatForm_encryption(unittest.TestCase):
#数据准备：上传影片，影片名称是Autotest
# #添加分类，分类名称是Autotest
#新增影片，影片名称是Autotest

    def setUp(self):
        self.main_url = "http://play-api.tctest0.com"#环境切换
        login_url = self.main_url + "/manager/1.0/login"
        login_data = {"account": "zdh", "password": "e10adc3949ba59abbe56e057f20f883e"}
        login_headers = {'Platform-Code': 'application/x-www-form-urlencoded'}
        login_response = requests.post(url=login_url, data=login_data, headers=login_headers)
        # print(login_response.status_code)
        # print(login_response.text)
        self.token = login_response.json().get('data').get('token')



    def test_login(self):
        #登录

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
        print('高清影片后台登录成功')

    def test_FilmEncryption(self):
        #高清加密菜单
        #查询
        movietype_url = self.main_url+"/manager/1.0/queryMovieList?title=Aototest&pageNum=1&pageSize=10&displayType=1"
        print(self.token)
        movietype_headers = {'token':self.token}
        movietype_respones = requests.get(url=movietype_url,headers = movietype_headers)
        print(movietype_respones.json())
        m_id = int(movietype_respones.json().get('data').get('data')[0].get('id'))

        self.assertEqual(movietype_respones.status_code, 200)
        self.assertEqual(movietype_respones.json().get('msg'),'成功')
        print('进入高清加密菜单')

        #加密按钮
        encryptFile_url = self.main_url + "/manager/1.0/encryptFile"
        encryptFile_headers = {'token': self.token,'Platform-Code': 'application/x-www-form-urlencoded'}
        encryptFile_data = {"id": m_id}
        encryptFile_respones = requests.post(url=encryptFile_url, data=encryptFile_data, headers=encryptFile_headers)
        # print(login_encryptFile_url_respones.json().get('meg'))
        #print(encryptFile_respones.json())
        #print(encryptFile_respones.status_code)
        self.assertEqual(encryptFile_respones.status_code, 200)
        self.assertEqual(encryptFile_respones.json().get('msg'), '成功')

        queryMovieListA_url = self.main_url+"/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        queryMovieListA_headers = {'token':self.token}
        queryMovieListA_respones = requests.get(url=queryMovieListA_url,headers = queryMovieListA_headers)
        #print(queryMovieListA_url_respones.json().get('meg'))
        #print(queryMovieListA_respones.json())
        #print(queryMovieListA_respones.status_code)
        self.assertEqual(queryMovieListA_respones.status_code, 200)
        self.assertEqual(queryMovieListA_respones.json().get('msg'),'成功')
        print('加密菜单-加密影片成功')

        #编辑按钮
        updateMovie_url = self.main_url + "/manager/1.0/updateMovie"
        updateMovie_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        updateMovie_data = {"id": m_id,'title':'Aototest2','sorted':1,'filmType':0}
        updateMovie_respones = requests.put(url=updateMovie_url, data=updateMovie_data, headers=updateMovie_headers)
        # print(login_updateMovie_url_respones.json().get('meg'))
        print(updateMovie_respones.json())
        print(updateMovie_respones.status_code)
        self.assertEqual(updateMovie_respones.status_code, 200)
        self.assertEqual(updateMovie_respones.json().get('msg'), '成功')

        queryMovieListB_url = self.main_url + "/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        queryMovieListB_headers = {'token': self.token}
        queryMovieListB_respones = requests.get(url=queryMovieListB_url, headers=queryMovieListB_headers)
        # print(queryMovieListB_url_respones.json().get('meg'))
        # print(queryMovieListB_respones.json())
        # print(queryMovieListB_respones.status_code)
        self.assertEqual(queryMovieListB_respones.status_code, 200)
        self.assertEqual(queryMovieListB_respones.json().get('msg'), '成功')
        print('加密菜单-编辑影片成功')

        #上架按钮
        updateMovieStatusA_url = self.main_url + "/manager/1.0/updateMovieStatus"
        updateMovieStatusA_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        updateMovieStatusA_data = {"id": m_id,'status':1}
        updateMovieStatusA_respones = requests.put(url=updateMovieStatusA_url, data=updateMovieStatusA_data, headers=updateMovieStatusA_headers)
        # print(login_updateMovieStatusA_url_respones.json().get('meg'))
        print(updateMovieStatusA_respones.json())
        print(updateMovieStatusA_respones.status_code)
        self.assertEqual(updateMovieStatusA_respones.status_code, 200)
        self.assertEqual(updateMovieStatusA_respones.json().get('msg'), '成功')

        queryMovieListB_url = self.main_url + "/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        queryMovieListB_headers = {'token': self.token}
        queryMovieListB_respones = requests.get(url=queryMovieListB_url, headers=queryMovieListB_headers)
        # print(queryMovieListB_url_respones.json().get('meg'))
        # print(queryMovieListB_respones.json())
        # print(queryMovieListB_respones.status_code)
        self.assertEqual(queryMovieListB_respones.status_code, 200)
        self.assertEqual(queryMovieListB_respones.json().get('msg'), '成功')
        print('加密菜单-上架影片成功')

        # 下架按钮
        updateMovieStatusB_url = self.main_url + "/manager/1.0/updateMovieStatus"
        updateMovieStatusB_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        updateMovieStatusB_data = {"id": m_id, 'status': 0}
        updateMovieStatusB_respones = requests.put(url=updateMovieStatusB_url, data=updateMovieStatusB_data, headers=updateMovieStatusB_headers)
        # print(login_updateMovieStatusB_url_respones.json().get('meg'))
        print(updateMovieStatusB_respones.json())
        print(updateMovieStatusB_respones.status_code)
        self.assertEqual(updateMovieStatusB_respones.status_code, 200)
        self.assertEqual(updateMovieStatusB_respones.json().get('msg'), '成功')

        queryMovieListC_url = self.main_url + "/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        queryMovieListC_headers = {'token': self.token}
        queryMovieListC_respones = requests.get(url=queryMovieListC_url, headers=queryMovieListC_headers)
        # print(queryMovieListC_url_respones.json().get('meg'))
        # print(queryMovieListC_respones.json())
        # print(queryMovieListC_respones.status_code)
        self.assertEqual(queryMovieListC_respones.status_code, 200)
        self.assertEqual(queryMovieListC_respones.json().get('msg'), '成功')
        print('加密菜单-下架影片成功')

        # 删除按钮
        deleteMovie_url = self.main_url + "/manager/1.0/deleteMovie/"+str(m_id)
        deleteMovie_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        #deleteMovie_data = {"id": m_id, 'status': 0}
        deleteMovie_respones = requests.delete(url=deleteMovie_url, headers=deleteMovie_headers)
        # print(login_deleteMovie_url_respones.json().get('meg'))
        print(deleteMovie_respones.json())
        print(deleteMovie_respones.status_code)
        self.assertEqual(deleteMovie_respones.status_code, 200)
        self.assertEqual(deleteMovie_respones.json().get('msg'), '成功')

        queryMovieListD_url = self.main_url + "/manager/1.0/queryMovieList?pageNum=1&pageSize=10&displayType=1"
        queryMovieListD_headers = {'token': self.token}
        queryMovieListD_respones = requests.get(url=queryMovieListD_url, headers=queryMovieListD_headers)
        # print(queryMovieListD_url_respones.json().get('meg'))
        # print(queryMovieListD_respones.json())
        # print(queryMovieListD_respones.status_code)
        self.assertEqual(queryMovieListD_respones.status_code, 200)
        self.assertEqual(queryMovieListD_respones.json().get('msg'), '成功')
        print('加密菜单-删除影片成功')

    def test_ClassifiedManagement(self):
        #分类管理
        login_movietype_url = self.main_url+"/movietype/1.0/list?pageNum=1&pageSize=10"
        login_movietype_headers = {'token':self.token}
        login_movietype_respones = requests.get(url=login_movietype_url,headers = login_movietype_headers)
        #print(login_movietype_url_respones.json().get('meg'))
        #print(login_movietype_respones.json())
        #print(login_movietype_respones.status_code)
        self.assertEqual(login_movietype_respones.status_code, 200)
        self.assertEqual(login_movietype_respones.json().get('msg'),'成功')
        print('高清影片分类管理页面')

        #搜索分类
        movietype_url = self.main_url + "/movietype/1.0/list?name=Aototest&pageNum=1&pageSize=10"
        movietype_headers = {'token':self.token}
        movietype_respones = requests.get(url=movietype_url,headers = movietype_headers)
        print(movietype_respones.json())
        n_id = int(movietype_respones.json().get('data').get('data')[0].get('id'))
        print('搜索分类')
        self.assertEqual(movietype_respones.status_code, 200)
        self.assertEqual(movietype_respones.json().get('msg'),'成功')

        # 编辑按钮
        update_url = self.main_url + "/movietype/1.0/update"
        update_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        update_data = {"id": n_id,'name':'Aototest1','sort':1}
        update_respones = requests.put(url=update_url, data=update_data, headers=update_headers)
        # print(login_update_url_respones.json().get('meg'))
        print(update_respones.json())
        print(update_respones.status_code)
        self.assertEqual(update_respones.status_code, 200)
        self.assertEqual(update_respones.json().get('msg'), '成功')

        listA_url = self.main_url + "/movietype/1.0/list?name=Aototest&pageNum=1&pageSize=10"
        listA_headers = {'token': self.token}
        listA_respones = requests.get(url=listA_url, headers=listA_headers)
        # print(listA_url_respones.json().get('meg'))
        # print(listA_respones.json())
        # print(listA_respones.status_code)
        self.assertEqual(listA_respones.status_code, 200)
        self.assertEqual(listA_respones.json().get('msg'), '成功')
        print('高清影片分类管理菜单-编辑分类按钮')

     # 停用按钮
        updateA_url = self.main_url + "/movietype/1.0/update"
        updateA_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        updateA_data = {"id": n_id, 'status': 0}
        updateA_respones = requests.put(url=updateA_url, data=updateA_data, headers=updateA_headers)
        # print(login_updateA_url_respones.json().get('meg'))
        print(updateA_respones.json())
        print(updateA_respones.status_code)
        self.assertEqual(updateA_respones.status_code, 200)
        self.assertEqual(updateA_respones.json().get('msg'), '成功')

        listB_url = self.main_url + "/movietype/1.0/list?pageNum=1&pageSize=10"
        listB_headers = {'token': self.token}
        listB_respones = requests.get(url=listB_url, headers=listB_headers)
        # print(listB_url_respones.json().get('meg'))
        # print(listB_respones.json())
        # print(listB_respones.status_code)
        self.assertEqual(listB_respones.status_code, 200)
        self.assertEqual(listB_respones.json().get('msg'), '成功')
        print('高清影片分类管理菜单-停用分类按钮')

        #启用按钮
        updateB_url = self.main_url + "/movietype/1.0/update"
        updateB_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        updateB_data = {"id": n_id,'status':1}
        updateB_respones = requests.put(url=updateB_url, data=updateB_data, headers=updateB_headers)
        # print(login_updateB_url_respones.json().get('meg'))
        print(updateB_respones.json())
        print(updateB_respones.status_code)
        self.assertEqual(updateB_respones.status_code, 200)
        self.assertEqual(updateB_respones.json().get('msg'), '成功')

        listB_url = self.main_url + "/movietype/1.0/list?pageNum=1&pageSize=10"
        listB_headers = {'token': self.token}
        listB_respones = requests.get(url=listB_url, headers=listB_headers)
        # print(listB_url_respones.json().get('meg'))
        # print(listB_respones.json())
        # print(listB_respones.status_code)
        self.assertEqual(listB_respones.status_code, 200)
        self.assertEqual(listB_respones.json().get('msg'), '成功')
        print('高清影片分类管理菜单-启用分类按钮')

        # 删除按钮
        delete_url = self.main_url + "/movietype/1.0/delete?id="+str(n_id)
        delete_headers = {'token': self.token, 'Platform-Code': 'application/x-www-form-urlencoded'}
        #delete_data = {"id": n_id, 'status': 0}
        delete_respones = requests.delete(url=delete_url, headers=delete_headers)
        # print(login_delete_url_respones.json().get('meg'))
        print(delete_respones.json())
        print(delete_respones.status_code)
        self.assertEqual(delete_respones.status_code, 200)
        self.assertEqual(delete_respones.json().get('msg'), '成功')

        queryMovieListD_url = self.main_url + "/movietype/1.0/list?pageNum=1&pageSize=10"
        queryMovieListD_headers = {'token': self.token}
        queryMovieListD_respones = requests.get(url=queryMovieListD_url, headers=queryMovieListD_headers)
        # print(queryMovieListD_url_respones.json().get('meg'))
        # print(queryMovieListD_respones.json())
        # print(queryMovieListD_respones.status_code)
        self.assertEqual(queryMovieListD_respones.status_code, 200)
        self.assertEqual(queryMovieListD_respones.json().get('msg'), '成功')
        print('高清影片分类管理菜单-删除分类按钮')

    def test_Film_Management_in_Live_Studio(self):
        # 直播间影片管理
        playback_queryA_url = self.main_url + "/playback/1.0/list/query?name=Aototest&pageNum=1&pageSize=10&displayType=1"
        playback_queryA_headers = {'token': self.token}
        playback_queryA_respones = requests.get(url=playback_queryA_url, headers=playback_queryA_headers)
        # print(playback_query_respones.json())
        self.assertEqual(playback_queryA_respones.status_code, 200)
        self.assertEqual(playback_queryA_respones.json().get('msg'), '成功')
        x_id = int(playback_queryA_respones.json().get('data').get('data')[0].get('id'))

        # 加密
        encryptFile_url = self.main_url + "/playback/1.0/encryptFile"
        encryptFile_headers = {'token': self.token}
        encryptFile_data = {'id': x_id}
        encryptFile_respones = requests.post(url=encryptFile_url, data=encryptFile_data, headers=encryptFile_headers)
        print(encryptFile_respones.text)
        self.assertEqual(encryptFile_respones.status_code, 200)
        self.assertEqual(encryptFile_respones.json().get('msg'), '成功')

        queryMovieListB_url = self.main_url + "/playback/1.0/list/query?name=Aototest&pageNum=1&pageSize=10&displayType=1"
        queryMovieListB_headers = {'token': self.token}
        queryMovieListB_respones = requests.get(url=queryMovieListB_url, headers=queryMovieListB_headers)
        # print(queryMovieListB_url_respones.json().get('meg'))
        # print(queryMovieListB_respones.json())
        # print(queryMovieListB_respones.status_code)
        self.assertEqual(queryMovieListB_respones.status_code, 200)
        self.assertEqual(queryMovieListB_respones.json().get('msg'), '成功')
        print('直播间影片管理-加密影片')
        #
        # 编辑
        playback_update_url = self.main_url + "/playback/1.0/update"
        playback_update_headers = {'token': self.token}
        playback_update_data = {'id': x_id, 'name': 'Aototest1', 'sort': 1}
        playback_update_respones = requests.put(url=playback_update_url, data=playback_update_data,
                                                headers=playback_update_headers)
        # print(playback_update_respones.json())
        self.assertEqual(playback_update_respones.status_code, 200)
        self.assertEqual(playback_update_respones.json().get('msg'), '成功')

        playback_queryB_url = self.main_url + "/playback/1.0/list/query?name=Aototest&pageNum=1&pageSize=10&displayType=1"
        playback_queryB_headers = {'token': self.token}
        playback_queryB_respones = requests.get(url=playback_queryB_url, headers=playback_queryB_headers)
        # print(playback_queryB_url_respones.json().get('meg'))
        # print(playback_queryB_respones.json())
        # print(playback_queryB_respones.status_code)
        self.assertEqual(playback_queryB_respones.status_code, 200)
        self.assertEqual(playback_queryB_respones.json().get('msg'), '成功')
        print('直播间影片管理-编辑影片')

        # 删除
        playback_delete_url = self.main_url + "/playback/1.0/delete?id=" + str(x_id)
        playback_delete_headers = {'token': self.token}
        playback_delete_respones = requests.delete(url=playback_delete_url, headers=playback_delete_headers)
        # print(playback_delete_respones.json())
        self.assertEqual(playback_delete_respones.status_code, 200)
        self.assertEqual(playback_delete_respones.json().get('msg'), '成功')

        playback_queryC_url = self.main_url + "/playback/1.0/list/query?&pageNum=1&pageSize=10&displayType=1"
        playback_queryC_headers = {'token': self.token}
        playback_queryC_respones = requests.get(url=playback_queryC_url, headers=playback_queryC_headers)
        # print(playback_queryC_url_respones.json().get('meg'))
        # print(playback_queryC_respones.json())
        # print(playback_queryC_respones.status_code)
        self.assertEqual(playback_queryC_respones.status_code, 200)
        self.assertEqual(playback_queryC_respones.json().get('msg'), '成功')
        print('直播间影片管理-删除影片')


    def test_data_statistics(self):
        # 数据统计
        queryMovieStatsListA_url = self.main_url + "/manager/1.0/queryMovieStatsList?pageNum=1&pageSize=10"
        queryMovieStatsListA_headers = {'token': self.token}
        queryMovieStatsListA_respones = requests.get(url=queryMovieStatsListA_url, headers=queryMovieStatsListA_headers)
        # print(playback_query_respones.json())
        self.assertEqual(queryMovieStatsListA_respones.status_code, 200)
        self.assertEqual(queryMovieStatsListA_respones.json().get('msg'), '成功')

        # 搜索美剧
        queryMovieStatsListB_url = self.main_url + "/manager/1.0/queryMovieStatsList?title=%E7%BE%8E%E5%89%A7&pageNum=1&pageSize=10"
        queryMovieStatsListB_headers = {'token': self.token}
        queryMovieStatsListB_respones = requests.get(url=queryMovieStatsListB_url, headers=queryMovieStatsListB_headers)
        # print(queryMovieStatsListB_respones.text)
        self.assertEqual(queryMovieStatsListB_respones.status_code, 200)
        self.assertEqual(queryMovieStatsListB_respones.json().get('msg'), '成功')
        print('高清影片数据统计页面')


    def tearDown(self):
            #print('接口测试通过')
            pass

# if __name__ == "__main__":
#     unittest.main()