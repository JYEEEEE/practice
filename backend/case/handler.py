"""
用例文本管理

测试用例
1. 文本描述
2. 测试代码

数据结构
用例编号： code （唯一） string
用例内容： content   string
用例状态： status (启用或者禁用)  int
//用例的创建人： owner
创建时间： created_dt   datetime
//用例的编辑人： editor
编辑时间： updated_dt  datetime
[{code:,content:,status:,}]

实现4个功能
1. 新增
新增一个测试用例的文本
输入参数
code/content/status
输出：
feedback:
1    成功保存
0    服务器异常
-1   编码code不唯一
-2   元素之一为空
...

2. 编辑
输入参数：
code
输出：
feedback/code/content/status/

3. 删除
4. 查询
"""

import json
import pymongo
import time
from tornado.web import RequestHandler

mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = mongo_client['cases']
table_case = db.test_cases


class NewCase(RequestHandler):
    """
    新增用例文本
    传入：code/content
    输出：feedback：
            1    成功保存
            0    服务器异常
            -1   编码code不唯一
            -2   元素之一为空
    """

    def get(self):
        self.render('../templates/case/add.html')

    def post(self):
        ret_dict = {}

        code = self.get_argument('code')
        content = self.get_argument('content')

        ret_dict['feedback'] = 0
        if not code or not content:
            ret_dict['feedback'] = -2
            self.write(json.dumps(ret_dict))
            return

        global table_case
        code_result = table_case.find_one({'code': code})
        if code_result:
            ret_dict['feedback'] = -1
            self.write(json.dumps(ret_dict))
            return
        new_case = table_case.insert_one(
            {'code': code,
             'content': content,
             'created_dt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
             'updated_dt': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
             }
        )
        if new_case.inserted_id:
            ret_dict['feedback'] = 1

        self.write(json.dumps(ret_dict))
        print(ret_dict)
        return


class EditCase(RequestHandler):
    """
    编辑用例文本
    传入：code
    输出：feedback：
            1    成功找到
            0    服务器异常
            -1   code不存在
         case
    """

    def get(self):
        self.render('../templates/case/edit.html')

    def post(self):
        ret_dict = {}
        global table_case

        code = self.get_argument('code')
        code_result = table_case.find_one({'code': code})

        ret_dict['feedback'] = 0
        if code_result:
            ret_dict['feedback'] = 1
            case = [{'code': code, 'content': code_result['content']}]
            self.write(json.dumps(ret_dict))
            return case
        if not code_result:
            ret_dict['feedback'] = -1
            self.write(json.dumps(ret_dict))
            return
