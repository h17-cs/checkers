import tornado.web
from tornado.gen import coroutine
from react.render import render_component
from DatabaseManager import DatabaseManager, DatabaseType
import config as cfg
import os,sys,time,threading
from ServerManager import ServerManager

class BaseHandle(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, PUT, OPTIONS")
        self.set_header("Content-Type", "application/json")
    def options(self):
        self.set_status(200)
        self.finish()

class AddUserHandler(BaseHandle):
    def prepare(self):
        super(AddUserHandler, self).prepare()
        self.json_data = None
        try:
            self.json_data = tornado.escape.json_decode(self.request.body)
            print(self.json_data)
            print(self.request)
        except ValueError:
            pass
    def get_argument(self, arg, default=None):
        if (    self.request.method in ['POST', 'PUT'] \
                and self.json_data \
                and (self.json_data["message_type"] == 3) ):
            if arg in self.json_data.keys():
                self.json_data['body'][arg]
            else:
                return None
        else:
            return super(AddUserHandler, self).get_argument(arg, default)
    '''
    def write_message(self, message):
        self.write_message(message)
    '''
    def post(self):
        sm = ServerManager.instance
        usernm = self.get_argument('username', None)
        passwd = self.get_argument('password', None)
        rval = True
        if not usernm is None and not passwd is None:
            rval &= sm.addUser(usernm, password)
        else:
            rval = False
        
        stat = 0
        msg = ""
        if rval:
        # Status 200: User success
            stat = 200
            msg = "Account Created"
        else:
        # Status 400: User error
            stat = 400
            msg = "Failed to create account"

        self.set_status(stat)
        self.finish({"resp" : msg})

class createPublicGameHandler(BaseHandler):
    def prepare(self):
        super(createPublicGameHandler, self).prepare()
    def get(self, slug):
        user = self.get_argument('userid', None)
        
        ServerManager.instance.requestPublicGame(user)
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################

class createPrivateGameHandler(BaseHandler):
    def prepare(self):
        super(createPrivateGameHandler, self).prepare()
    def get(self, slug):
        user = self.get_argument('userid', None)
        
        ServerManager.instance.requestPrivateGame(userCreated)
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################

class loginHandler(BaseHandler):
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
        if (self.request.method in ['POST', 'PUT'] and self.json_data):
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

class ContentHandler(BaseHandler):
    def get(self):
        rendered = render_component(os.path.join(os.getcwd(), 'local_files', 'checkmate-front-end', 'src', 'Register.js'),{},to_static_markup=False,)
        self.render('/home/salieri/Desktop/checkers/dev/back-end/local_files/checkmate-front-end/public/index.html', rendered=rendered)
