# coding=utf-8
import traceback

import sys
from flask import current_app
from pip._vendor import requests


class uia():
    def __init__(self):
        pass

    # 验证用户身份
    def authentication(self, login_name, login_password):
        user_info = "xh=" + login_name + "&" + "password=" + login_password
        r = requests.post("http://bysj.cuit.edu.cn:8098/Interface/TaoRan_Interface.svc/CheckUserPassword",
                          data=user_info)
        r.encoding = 'utf-8'
        s = r.text
        strl = ''
        for x in s[1:]:
            strl += x
        login_status = eval(strl)
        return login_status["msg"]

    # 无密码验证用户身份
    def nopass_authen(self, login_name):
        user_info1 = "xh=" + login_name
        j = requests.post("http://bysj.cuit.edu.cn:8098/Interface/TaoRan_Interface.svc/GetUserInfo",
                          data=user_info1)
        j.encoding = 'utf-8'
        d = j.text

        # 将接受到的字符转化为字符串
        strs = ''
        for x in d[1:]:
            strs += x

        # 再将字符串字典化
        try:
            stu_status = eval(strs)  # 状态字典
        except Exception as e:
            return 'false'
        return stu_status["msg"]

    # 得到学生信息
    def get_student_info(self, login_name):
        user_info1 = "xh=" + login_name
        j = requests.post("http://bysj.cuit.edu.cn:8098/Interface/TaoRan_Interface.svc/GetUserInfo",
                          data=user_info1)
        j.encoding = 'utf-8'
        d = j.text

        # 将接受到的字符转化为字符串
        strs = ''
        for x in d[1:]:
            strs += x

        # 再将字符串字典化
        stu_status = eval(strs)  # 状态字典

        # 以下是为了解决子字典转化为字符串后再转化为独立字典时遇到的
        # 错误：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
        reload(sys)
        sys.setdefaultencoding('utf8')
        # 解决结束

        # 字符串化和字典化
        try:
            strda = str(stu_status["data"])
            stu_data = eval(strda)
        except Exception as e:
            return 'false'
        return stu_data
