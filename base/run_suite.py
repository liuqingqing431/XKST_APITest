# 导包
import time
import unittest
from base.XKST_firstpage import TestMethod
import HTMLTestRunner


# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestMethod))


# 指定报告路径
report = "../report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report, "wb") as fb:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner.HTMLTestRunner(fb, title="小开刷题接口测试报告")

    # 执行测试套件
    runner.run(suite)
