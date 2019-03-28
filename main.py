#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler


PORT = 8080


class FaceCount(RequestHandler):
    def get(self):
        pass

    def post(self):
        pass


def main():
    app = tornado.web.Application([
        (r'/count', FaceCount)
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
