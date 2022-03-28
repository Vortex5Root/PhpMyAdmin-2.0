from threading import Thread
from API.DB_API import DB
from Configs.Config import Config
from Socket.sock_sv import Server_API
from Treminal import cmd
class __Start__():
    dbs = DB()
    conf = Config()
    def __init__(self):
        self.Start_Config()
        self.Start_WebApi()
        self.Start_Socket()
    def Debuger_Premissoes(self):
        try:
            debug = []
            debug = self.conf.Check_Users_Premes()
            if debug == False:
                self.conf.Create_Premes_Register_Config()
            elif debug != None:
                for a in debug:
                    print(a)
                return False
            else:
                return True
        except:
            return "Config Not Create"
    def Start_Config(self):
        debug = self.Debuger_Premissoes()
        print(debug)
        if debug == False:
            exit()
        elif debug == "Config Not Create":
            self.conf.Create_Config()
            self.conf.Create_Premes_Register_Config()
    def Start_Socket(self):
        socket_api = Server_API()
        try:
            Thread(target=socket_api.Server_Start, args=('12', '12')).start()
            cmd()
        except EOFError:
            print(EOFError)
    def Start_WebApi(self):
        try:
            Thread(target=self.test, args=('12', '12')).start()
        except EOFError:
            print(EOFError)
    def test(self,asd,a):
        from WebSocket.WebPage import WebAPI
start = __Start__()