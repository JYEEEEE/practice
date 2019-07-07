"""
实现注册和登录
"""
import json
from tornado.web import RequestHandler
import pymongo

mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = mongo_client['users']
table = db.users

class Register(RequestHandler):
    """
    input: {'login_name': xxxx, 'login_passwd': xxxx}
    return: 1 注册成功， -1 该用户名已被注册， -2 请完整填写注册信息
    """
    def get(self):
        self.render('../templates/auth/register.html')

    def post(self):
        ret_dict = {'code': 0}
        login_name = self.get_argument('login_name','')
        login_passwd = self.get_argument('login_passwd','')

        print('register', login_name, login_passwd)

        if not login_name or not login_passwd:
            ret_dict['code'] = -2
            self.write(json.dumps(ret_dict))
            return
        name_result = table.find_one({'login_name': login_name})
        print(name_result)
        if name_result:
            ret_dict['code'] = -1
            self.write(json.dumps(ret_dict))
            return

        new_user = table.insert_one({'login_name':login_name,'login_passwd':login_passwd})
        if new_user.inserted_id:
            ret_dict['code'] = 1
            self.write(json.dumps(ret_dict))
            return


class Login(RequestHandler):
    """
    input: {'login_name': xxxx, 'login_passwd': xxxx}
    do: 去数据库查询，有没有该用户， 密码对不对
    return: code: -1 , 没有改用户， -2 密码不对
    """
    def get(self):
        self.render('../templates/auth/login.html')

    def post(self):
        ret_dict = {'code': 0}
        login_name = self.get_argument('login_name','')
        login_passwd = self.get_argument('login_passwd','')
        name_result = table.find_one({'login_name':login_name})
        passwd_result = table.find_one({'login_passwd':login_passwd})
        if name_result:
            if passwd_result:
                ret_dict['code'] = 1
            else:
                ret_dict['code'] = -2
        else:
            ret_dict['code'] = -1

        self.write(json.dumps(ret_dict))

