import tornado.web
from tornado.gen import coroutine
from react.render import render_component
import config as cfg
import os,sys,time,threading
import ServerManager
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

    def post(self):
        sm = ServerManager.instance
        usernm = self.get_body_argument('username', None)
        passwd = self.get_body_argument('password', None)
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

class createPublicGameHandler(BaseHandle):
    def prepare(self):
        super(createPublicGameHandler, self).prepare()
    def get(self, slug):
        user = self.get_query_argument('userid', None)
        retval = True
        if userid is not None:
            retval &= ServerManager.instance.requestPrivateGame(user)
        else:
            retval = False
        
        stat = 0
        msg = ""
        if rval:
        # Status 200: User success
            stat = 200
            msg = "Awaiting Public Game"
        else:
        # Status 400: User error
            stat = 400
            msg = "Failure to create Public Game"

        self.set_status(stat)
        self.finish({"resp" : msg})
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################

class createPrivateGameHandler(BaseHandle):
    def prepare(self):
        super(createPrivateGameHandler, self).prepare()
    def get(self, slug):
        user = self.get_query_argument('userid', None)
        retval = True
        if userid is not None:
            retval &= ServerManager.instance.requestPrivateGame(user)
        else:
            retval = False
        
        stat = 0
        msg = ""
        if rval:
        # Status 200: User success
            stat = 200
            msg = "Awaiting private game"
        else:
        # Status 400: User error
            stat = 400
            msg = "Failure to create Private Game"

        self.set_status(stat)
        self.finish({"resp" : msg})
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################

class loginHandler(BaseHandle):
    def post(self):
        sm = ServerManager.instance
        usernm = self.get_body_argument('username', None)
        passwd = self.get_body_argument('password', None)
        rval = True
        if not usernm is None and not passwd is None:
            rval &= sm.checkUser(usernm, password)
        else:
            rval = False
        
        stat = 0
        msg = ""
        if rval:
        # Status 200: User success
            stat = 200
            msg = "Success"
        else:
        # Status 400: User error
            stat = 400
            msg = "Failed to log in"

        self.set_status(stat)
        self.finish({"resp" : msg})

class ContentHandler(BaseHandle):
    def get(self):
        rendered = render_component(os.path.join(os.getcwd(), 'local_files', 'checkmate-front-end', 'src', 'Register.js'),{},to_static_markup=False,)
        self.render('/home/salieri/Desktop/checkers/dev/back-end/local_files/checkmate-front-end/public/index.html', rendered=rendered)
