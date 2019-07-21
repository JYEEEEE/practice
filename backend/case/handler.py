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


实现4个功能
1. 新增
新增一个测试用例的文本
输入参数
code/content/status
输出：
feedback:
0    成功保存
1    服务器异常
2    编码code不唯一
3    content为空
...

2. 编辑
输入参数：
code
输出：
feedback/code/content/status/

3. 删除
4. 查询
"""