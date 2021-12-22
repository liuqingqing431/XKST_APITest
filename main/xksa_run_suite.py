# 导包
import time
import unittest
from main.test_run import RunTest
import HTMLTestRunner


# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunTest))
print(RunTest)


# 指定报告路径
report = "../report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report, "wb") as fb:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner.HTMLTestRunner(fb, title="小开上岸接口测试报告")

    # 执行测试套件
    runner.run(suite)
