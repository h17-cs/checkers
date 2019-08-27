import tornado.web
import json
from tornado.gen import coroutine
from react.render import render_component
import config as cfg
import os
import sys
import time
import threading


class BaseHandle(tornado.web.RequestHandler):
    game_manager = None

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods",
                        "POST, GET, PUT, OPTIONS")
        self.set_header("Content-Type", "application/json")

    def get_message_type(self):
        obj = self.request.body.decode('ascii')
        parse = json.loads(obj)
        return parse["message_type"] if json is not None else None

    def get_body_argument(self, query, **kwargs):
        obj = self.request.body.decode('ascii')
        parse = json.loads(obj)
        #bod = super().get_body_argument('body', None)
        #print("\033[31;1m", parse, "\033[0m")
        #print("\033[31;1m" ,dir(parse), "\033[0m")
        bod = parse["body"]
        if bod is None:
            print("No body in message")
            return None
        if query in bod.keys():
            return bod[query]
        else:
            return None

    def options(self):
        self.set_status(200)
        self.finish()


class AddUserHandler(BaseHandle):
    def prepare(self):
        super(AddUserHandler, self).prepare()
        self.json_data = None
        try:
            self.json_data = tornado.escape.json_decode(self.request.body)
            # print(self.json_data)
            # print(self.request)
        except ValueError:
            pass

    def post(self):
        sm = self.game_manager
        # print("Message of type ", self.get_message_type())
        usernm = self.get_body_argument('username')
        passwd = self.get_body_argument('password')
        # print("add user request with u:%s, p:%s"%(usernm,passwd))
        rval = True
        if not usernm is None and not passwd is None:
            rval &= sm.addUser(usernm, passwd)
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
        self.finish({"resp": msg})


class createPublicGameHandler(BaseHandle):
    def prepare(self):
        super(createPublicGameHandler, self).prepare()

    def get(self):
        sm = self.game_manager
        user = self.get_query_argument('userid')
        print("create public request with u:%s" % (user))
        retval = True
        if user is not None:
            retval &= sm.requestPublicGame(user)
        else:
            retval = False

        stat = 0
        msg = ""
        if retval:
            # Status 200: User success
            stat = 200
            msg = "Awaiting Public Game"
        else:
            # Status 400: User error
            stat = 400
            msg = "Failure to create Public Game"

        self.set_status(stat)
        self.finish({"resp": msg})
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################


class createPrivateGameHandler(BaseHandle):
    def prepare(self):
        super(createPrivateGameHandler, self).prepare()

    def get(self):
        sm = self.game_manager
        user = self.get_query_argument('userid')
        print("create private request with u:%s" % (user))
        retval = True
        if user is not None:
            retval &= sm.requestPrivateGame(user)
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
        self.finish({"resp": msg})
        # await user auth at some point
        ##############################################
        # PASS DATA TO SOCKET FOR CENTRAL PROCESSING #
        ##############################################


class loginHandler(BaseHandle):
    def post(self):
        sm = self.game_manager
        print("Message of type ", self.get_message_type())
        usernm = self.get_body_argument('username')
        passwd = self.get_body_argument('password')
        print("login request with u:%s, p:%s" % (usernm, passwd))
        rval = True
        if not usernm is None and not passwd is None:
            rval &= sm.checkUser(usernm, passwd)
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
        self.finish({"resp": msg})


class descriptionHandler(BaseHandle):
    def get(self):
        desc_path = '/home/charles/checkers/dev/checkmate-front-end/src/components/About.js'
        rendered = render_component(desc_path)
        self.set_status = 200
        self.write(rendered)


class ContentHandler(BaseHandle):
    def get(self):
        rendered = render_component(os.path.join(os.getcwd(
        ), 'local_files', 'checkmate-front-end', 'src', 'Register.js'), {}, to_static_markup=False,)
        self.render(
            '/home/salieri/Desktop/checkers/dev/back-end/local_files/checkmate-front-end/public/index.html', rendered=rendered)
