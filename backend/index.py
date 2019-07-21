from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    """
    首页
    """

    def get(self):
        self.render('../templates/index.html')
