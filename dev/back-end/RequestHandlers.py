import tornado.web

class AddUserHandler(tornado.web.RequestHandler):
    def prepare(self):
        super(AddUserHandler, self).prepare()
        self.json_data = None
        try:
            self.json_data = tornado.escape.json_decode(self.request.body)
        except ValueError:
            pass
    def get_argument(self, arg, default=None):
        if self.request.method in ['POST', 'PUT'] and self.json_data:
            return self.json_data['body']['username']
        else:
            return super(AddUserHandler, self).get_argument(arg, default)
    def post(self):
        print(self.get_argument('', None))

class ContentHandler(tornado.web.RequestHandler):
    def get(self):
        print("get got")
