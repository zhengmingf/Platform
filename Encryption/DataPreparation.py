import time,os
from selenium import webdriver
import unittest
class DataPreparation(unittest.TestCase):
    # 数据准备：上传影片，影片名称是Autotest
    # #添加分类，分类名称是Autotest
    # 新增影片，影片名称是Autotest
    def test_DataPreparation(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\admin\AppData\Local\Google\Chrome\Application\chromedriver")
        driver.get("http://play-admin.tctest0.com/")
        driver.find_element_by_xpath(".//*[@id='app']/div/div/div/div[2]/div/form/div[1]/div/div[1]/input").send_keys('zdh1')
        driver.find_element_by_xpath(".//*[@id='app']/div/div/div/div[2]/div/form/div[2]/div/div/input").send_keys('123456')
        driver.find_element_by_xpath(".//*[@id='app']/div/div/div/div[2]/div/form/div[3]/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='HdVideo']/div[1]/div/div[2]/div[4]/button").click()
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys('Aototest')
        time.sleep(2)
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/span").click()
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/ul[2]/li[1]").click()
        # 上传图片
        driver.find_element_by_xpath(".//*[@id='UploadImg']/div[1]/div/button").click()
        time.sleep(1)
        os.system(r"C:\Users\admin\PycharmProjects\Platform\Encryption\updataPic.exe")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='UploadImg']/div[2]/button").click()
        # 上传影片
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[3]/div/div[2]/input").click()
        time.sleep(1)
        os.system(r"C:\Users\admin\PycharmProjects\Platform\Encryption\updataV.exe")
        time.sleep(2)
        driver.find_element_by_xpath("html/body/div[6]/div[2]/div/div/div[3]/div/button").click()
        time.sleep(15)
        print("影片加密模块，影片上传完成")
        # 数据准备：分类管理模块上传图片和影片
        driver.find_element_by_xpath(".//*[@id='LeftMenu']/ul/li/ul/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='HdVideo']/div[1]/div/div/div[5]/button").click()
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys("Aototest")
        driver.find_element_by_xpath(".//*[@id='UploadImg']/div[1]/div/button").click()
        time.sleep(1)
        os.system(r"C:\Users\admin\PycharmProjects\Platform\Encryption\updataPic.exe")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='UploadImg']/div[2]/button").click()
        time.sleep(8)
        driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(1)
        print("分类管理模块，分类图片上传完")

        # 数据准备：直播间影片管理模块上传影片
        driver.find_element_by_xpath(".//*[@id='LeftMenu']/ul/li/ul/li[3]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='HdVideo']/div[1]/div/div[2]/div[4]/button").click()
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys("Aototest")
        driver.find_element_by_xpath(".//div[2]/div/div/div[2]/form/div[2]/div/div[2]/input").click()
        time.sleep(1)
        os.system(r"C:\Users\admin\PycharmProjects\Platform\Encryption\updataV.exe")
        time.sleep(2)
        driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[3]/div/button").click()
        time.sleep(15)
        print("直播间影片管理模块，上传影片完成")
        driver.quit()
