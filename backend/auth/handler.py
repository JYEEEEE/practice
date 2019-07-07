"""
# todo
实现注册和登录

"""
from tornado.web import RequestHandler
import pymongo

mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = mongo_client['users']
table = db.users

class Register(RequestHandler):
    """
    input: {'login_name': xxxx, 'login_passwd': xxxx}
    """
    def post(self):
        login_name = self.get_argument('login_name')
        login_passwd = self.get_argument('login_passwd')
        new_user = table.insert_one({'login_name':login_name,'login_passwd':login_passwd})
        self.write(new_user)

class Login(RequestHandler):
    """
    input: {'login_name': xxxx, 'login_passwd': xxxx}
    do: 去数据库查询，有没有该用户， 密码对不对
    return: code: -1 , 没有改用户， -2 密码不对
    """
    def get(self):
        login_name = self.get_argument('login_name')
        login_passwd = self.get_argument('login_passwd')
        name_result = table.find_one({'login_name':login_name})
        passwd_result = table.find_one({'login_passwd':login_passwd})
        if name_result:
            if passwd_result:
                self.write(1)
            else:
                self.write(-2)
        else:
            self.write(-1)
