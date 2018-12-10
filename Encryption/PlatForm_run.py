import HTMLTestReportCN
import unittest
from PlatForm_encryption import PlatForm_encryption
from DataPreparation import DataPreparation
suite = unittest.TestSuite()
suite.addTest(DataPreparation('test_DataPreparation'))
suite.addTest(PlatForm_encryption('test_FilmEncryption'))
suite.addTest(PlatForm_encryption('test_ClassifiedManagement'))
suite.addTest(PlatForm_encryption('test_Film_Management_in_Live_Studio'))
suite.addTest(PlatForm_encryption('test_data_statistics'))



filePath ='D:\\Report_selemiun.html'       #确定生成报告的路径
fp = open(filePath,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=u'影片加密后台',
    #description='详细测试用例结果',    #不传默认为空
    tester=u"zhengming"     #测试人员名字，不传默认为QA
    )
#运行测试用例
runner.run(suite)