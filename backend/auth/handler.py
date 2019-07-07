"""
# todo
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
    return: 1 成功， 0 失败
    """
    def get(self):
        self.render('../templates/auth/register.html')

    def post(self):
        ret_dict = {'code': 0}
        login_name = self.get_argument('login_name','')
        login_passwd = self.get_argument('login_passwd','')
        new_user = table.insert_one({'login_name':login_name,'login_passwd':login_passwd})
        if new_user.inserted_id:
            ret_dict['code'] = 1

        print('register')
        self.write(json.dumps(ret_dict))

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

# -1 --> '-1'
# '-1' --> '"-1"'