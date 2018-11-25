import unittest, time, os
from util.HTMLTestRunner_cn import HTMLTestRunner
from config import description, reporttitle

path = os.getcwd()
case_path = path + '\\case'


def create_report(is_new):
    '''
    运行所有*_test.py文件中的test,生成报告
    :param is_new: n 覆盖旧的报告，y 根据时间格式生产新报告
    :return: 根据规则生成测试报告文件名，相对路径
    '''
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*test.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)
    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))

    # 如果是 y 报告名称插入时间，每次新增；如果是 n 每次生成的报告名称相同,会覆盖前一个报告
    if is_new == 'y':
        report_dir = path + '\\report\\%s.html' % now
    elif is_new == 'n':
        report_dir = path + '\\report\\HTMLtemplate.html'
    else:
        print('生成报个格式不对，只能输入【y】或【n】')
    re_open = open(report_dir, 'wb')
    runner = HTMLTestRunner(stream=re_open, title=reporttitle, description=description)
    runner.run(test_suit)


def run_case():
    '''
    运行所有*_test.py文件中的test,不生成报告（结果输出控制台）
    :return:
    '''
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*test.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)

    runner = unittest.TextTestRunner()
    runner.run(test_suit)
