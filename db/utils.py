"""
定义一个数据库工具类

要求：
无论何时获取数据库都得到同一个client，mongo_client['wjj']
c1 = c2 = ... = 数据库连接
"""


def step1(a, b):
    return 1


def step2(c, d):
    return 2


def step3(e, f):
    return 2


v = step1(1, 2)
v2 = step2(1, v)
v3 = step3(1, v2)
print(v3)


class Calc(object):

    def __init__(self, a, b, c, e):
        self.a = a
        self.b = b
        self.c = c
        self.e = e

    def step1(self, a, b):
        return 1

    def step2(self, c, d):
        return 2

    def step3(self, e, f):
        return 2

    def run(self):
        v = self.step1(self.a, self.b)
        v2 = self.step2(self.c, v)
        return self.step3(self.e, v2)


cal = Calc(1, 1, 1, 1)
ret = cal.run()
