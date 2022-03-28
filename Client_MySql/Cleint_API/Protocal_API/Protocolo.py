from socket import *
from threading import Thread

from Encode_API.Encrype_API import Hash
from Config_API.Configs_API import Config
class Protocolo_1():
    def __init__(self):
        self.conf = Config()
        self.connectos_Hendler = []
        self.actions = []
        self.returns = []
        self.priviasse_login = ''
        self.load_Privice_Logins()
        print(self.priviasse_login)
    def load_Privice_Logins(self):
        if self.conf.Check_Config('Connections','Hosts'):
            self.priviasse_login = self.conf.push_Config('Connections','Hosts')
        else:
            self.conf.add_Config('Connections','','Hosts')
    def add_Task(self,conn,command):
        self.actions.append('{'+conn+'} '+command)
    def Get_Retruns(self,host):
        for i in self.returns:
            if host == str(str(i).split(' ')[0]).replace('}', '').replace('{', ''):
                self.returns.remove(i)
                return str(str(i).split(' ')[1])
        return None
    def start_BackGroud_Client(self,conn,user_info):
        Thread(target=self.connect, args=(conn, user_info)).start()
    def connect(self,conn,user_info):
        Host,Port,hash = str(conn).split(':')[0],str(conn).split(':')[1],user_info
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((Host, Port))
            s.sendall(hash)
            while True:
                data = s.recv(4096).decode()
                if str(data) == 'loged':
                    while True:
                        for i in self.actions:
                            try:
                                if str(i).split(' ')[0] == '{'+conn+'}':
                                    s.sendall(str(str(i).split(' ')[1]).encode())
                                    while True:
                                        data = s.recv(4096).decode()
                                        if data != '':
                                            self.returns.append('{' + conn + '} ' + str(data))
                                            self.actions.remove(i)
                                            break
                                else:
                                    pass
                            except:
                                pass
                else:
                    self.returns.append('{'+conn+'}'+' Wrong User or password')
                    break
            self.returns.append('{'+conn+'}'+' Connectio TimeOut')