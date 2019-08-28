#Author : Danea

import unittest
import os
import HTMLTestRunner
import time

case_path = os.path.join(os.getcwd(),'case')
report_path= os.path.join(os.getcwd(),'report')

#获取所有测试用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
    print(discover)
    return discover

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # print(now)

    report_abs_path = os.path.join(report_path,"report"+now+".html")
    fp = open(report_abs_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="接口测试报告",description="详细如下")

    # runner = unittest.TextTestRunner()
    #
    runner.run(all_case())
