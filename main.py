"""
http client: request -> methods: ['GET', 'POST']

http server : app running -> ioloop -> listen port -> 'GET' request(url, args)


register: app start: url_list = ['']

C/S
request: client --> server
response: server --> client
"""
import os
import tornado.ioloop
import tornado.web

from backend.case.handler import NewCase, EditCase
from backend.home import MainHandler, MathAddHandler
from backend.auth.handler import Register, Login
from backend.index import IndexHandler


def make_app():
    setting = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
    )

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", MathAddHandler),
        (r"/register", Register),
        (r"/login", Login),
        (r"/index", IndexHandler),
        (r"/case/add", NewCase),
        (r"/case/edit", EditCase)
    ], **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
