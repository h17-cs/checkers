import os.path
from mimetypes import guess_type

import tornado.web
import tornado.httpserver

BASEDIR_NAME = os.path.dirname(__file__)
BASEDIR_PATH = os.path.abspath(BASEDIR_NAME)

FILES_ROOT = os.path.join(BASEDIR_PATH, 'files')


class FileHandler(tornado.web.RequestHandler):

    def get(self, path):
        file_location = os.path.join(FILES_ROOT, path)
        if not os.path.isfile(file_location):
            raise tornado.web.HTTPError(status_code=404)
        content_type, _ = guess_type(file_location)
        self.add_header('Content-Type', content_type)
        with open(file_location) as source_file:
            self.write(source_file.read())

app = tornado.web.Application([
    tornado.web.url(r"/(.+)", FileHandler),
])

http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(8080, address='localhost')
tornado.ioloop.IOLoop.instance().start()
