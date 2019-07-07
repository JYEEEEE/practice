# client --> url


from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello,world")

    def post(self):
        pass


# 加法: post: {'number1': 1, 'number2': 2}
class MathAddHandler(RequestHandler):
    def get(self):
        self.render('../templates/add.html')

    def post(self):
        n1 = self.get_argument('number1', 0)
        n2 = self.get_argument('number2', 0)
        operator = self.get_argument('operator', '+')
        if operator == '+':
            result = int(n1) + int(n2)
        elif operator == '-':
            result = int(n1) - int(n2)
        elif operator == '*':
            result = int(n1) * int(n2)
        elif operator == '/':
            result = int(n1) / int(n2)

        self.write(str(result))
