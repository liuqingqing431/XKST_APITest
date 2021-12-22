# coding:utf-8
import unittest
import json
import requests
from base.demo import RunMain
from base.mock_demo import mock_test
from jsonpath import jsonpath

class TestMethod(unittest.TestCase):
    def setUp(self):
        url = 'https://testxkst-api.kaikeba.com/kkb-etg-service/wechat/getTokenByUid/56327184'
        self.run = RunMain(url, 'GET')

    def test_01(self):
        url = 'https://test-etg-api.kaikeba.com/api/etg/land/etc/3634/getAndView'
        headers = {
            "token":"6832734793c3fb37bc89cf313c7309aa",
            "Content-Type":"application/json;charset=UTF-8",
            "Version":"2.0.0",
            "Device-Type":"1"
        }
        res = self.run.run_main(url, 'JSON', headers)
        print(res)
        # self.assertEqual(str(res['code']), '0', "测试失败")
        # self.assertEqual(res['msg'], 'Success', "测试失败")
        # self.assertIn('134', str(res['data']['paperTotalNum']), "测试失败")
        # print("这是第3个case")

    def test_02(self):
        global tokenl
        url = 'https://testxkst-api.kaikeba.com/kkb-etg-service/wechat/getTokenByUid/56327184'
        res = self.run.run_main(url, 'GET')
        print(res)
        tokenl = res['data']['token']
        #		name = jsonpath(res, "$..name")
        #		name = ', '.join(name)
        self.assertEqual(str(res['code']), '0', "测试失败")
        self.assertEqual(res['msg'], 'Success', "测试失败")
        #		self.assertIn('研究生', name, "测试失败")
        print("这是第1个case")

    #	@unittest.skip('test_02')
    def test_03(self):
        global header
        url = 'https://testxkst-api.kaikeba.com/kkb-etg-service/user-subject/subjects'
        header = {
            'Authorization': tokenl
        }
        res = self.run.run_main(url, 'GET', "", header)
        print(res)
        self.assertEqual(str(res['code']), '0', "测试失败")
        self.assertEqual(res['msg'], 'Success', "测试失败")
        self.assertIn('公务员', res['data']['projectName'], "测试失败")
        print("这是第2个case")

    #	@unittest.skip('test_02')
    def test_04(self):
        url = 'https://testxkst-api.kaikeba.com/kkb-etg-service/user-subject/notes'
        header = {
            'Authorization':'6d7c421fc4d811b2273144c3d7ac78ce|mobile:e6ed024a1b9c97395dc822ccc6ad283d'
        }
        data = {
            "categoryId": 10,
            "projectId": 134,
            "subjectId": 128
        }
        print(type(data))
        res = self.run.run_main(url, 'JSON', data, header)
        print(res)
        self.assertEqual(str(res['code']), '0', "测试失败")
        self.assertEqual(res['msg'], 'Success', "测试失败")
        self.assertIn('134', str(res['data']['paperTotalNum']), "测试失败")
        print("这是第3个case")


if __name__ == '__main__':
    unittest.main()
