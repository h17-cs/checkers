import tornado.web
from tornado.gen import coroutine
from react.render import render_component
from DatabaseManager import DatabaseManager, DatabaseType
import config as cfg
import os,sys,time,threading

class AddUserHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET")
    def prepare(self):
        dm = DatabaseManager(DatabaseType.CSV, cfg.db_addr)
        super(AddUserHandler, self).prepare()
        self.json_data = None
        try:
            self.json_data = tornado.escape.json_decode(self.request.body)
        except ValueError:
            pass
    def get_argument(self, arg, default=None):
        if self.request.method in ['POST', 'PUT'] and self.json_data and (self.json_data["message_type"] == 3):
            print("database post req recieved")
            dm = DatabaseManager(DatabaseType.CSV, cfg.db_addr)
            userToAdd = self.json_data['body']['username']
            passwdToAdd = self.json_data['body']['password']
            self.finish(str(dm.addUser(userToAdd, passwdToAdd)))
        else:
            return super(AddUserHandler, self).get_argument(arg, default)
    def write_message(self, message):
        self.write_message(message)
    def post(self):
        print(self.get_argument('', None))

class createPublicGameHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET")
    def prepare(self):
        super(createPublicGameHandler, self).prepare()
    def get(self, slug):
        userCreated = self.get_argument('userid', None)
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################

class createPrivateGameHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET")
    def prepare(self):
        super(createPrivateGameHandler, self).prepare()
    def get(self, slug):
        userCreated = self.get_argument('userid', None)
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################

class loginHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET")
    def prepare(self):
        super(loginHandler, self).prepare()
        self.json_data = None
        try:
            self.json_data = tornado.escape.json_decode(self.request.body)
        except ValueError:
            pass
    def get_argument(self, arg, default=None):
        if self.request.method in ['POST', 'PUT'] and self.json_data):
            userToAuth = self.json_data['body']['username']
            passwdToAuth = self.json_data['body']['password']
            ##############################################
            # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
            ##############################################
        else:
            return super(AddUserHandler, self).get_argument(arg, default)
    def write_message(self, message):
        self.write_message(message)
    def post(self):
        print(self.get_argument('', None))

class ContentHandler(tornado.web.RequestHandler):
    def get(self):
        rendered = render_component(os.path.join(os.getcwd(), 'local_files', 'checkmate-front-end', 'src', 'Register.js'),{},to_static_markup=False,)
        self.render('/home/salieri/Desktop/checkers/dev/back-end/local_files/checkmate-front-end/public/index.html', rendered=rendered)
