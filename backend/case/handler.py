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
import pymong
from tornado.web import RequestHandler
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = mongo_client['cases']
table_case = db.test_cases

class NewCase(RequestHandler):
    def get(self):
        self.render('../templates/case/add.html')

    def post(self):
        code = self.get_argument('code')
        content = self.get_argument('content')
        status = self.get_argument('status')

        ret_dict['feedback'] = 0
        if not code or not content or not status:
            ret_dict['feedback'] = -2
            self.write(json.dumps(ret_dict))
            return
        code_result = table.find_one({'code':code})
        if code_result:ret_dict['feedback'] = -1
            self.write(json.dumps(ret_dict))
            return
        new_case = table_case.insert_one({'code':code, 'content'})
