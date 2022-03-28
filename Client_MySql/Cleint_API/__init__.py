from Config_API.Configs_API import Config as conf
from Protocal_API import *
from Encode_API.Encrype_API import Hash
from Protocal_API.Protocolo import Protocolo_1
import sys

class Client():
    confi = conf()
    client = Protocolo_1()
    hashing = Hash()
    def __init__(self):
        self.opt = []
    def Terminal(self,args):
        try:
            host = args[args.index('-h')+1]
            login = args[args.index('-l')+1]
            l = self.hashing.hashing(str('login ' + str(login).split(':')[0] + ' ' + str(login).split(':')[1]).encode())
            auto_run = ''
            try:
                auto_run = args[args.index('-auto')+1]
            except:
                auto_run = ''
            if auto_run != '':
                self.client.start_BackGroud_Client(host,l)
                self.client.add_Task(host,auto_run)
            else:
                self.client.start_BackGroud_Client(host, l)
            while True:
                while True:
                    r = self.client.Get_Retruns()
                    if r != None:
                        print(r)
                    else:
                        break
                cmd = input('>')
                self.client.add_Task(host,cmd)
        except:
            print('[Treminal] python3 __init__.py -h <IP>:<Port> -l <User>:<Password> opt -auto <Un_Commnad>')
            return False
cl =Client()
args = str(sys.argv)
cl.Terminal(args)