import time
from socket import *
from Configs.Config import Config
from threading import Thread
from Socket.Socket_Encrype import Hash
from Ferramentas.function import Fun
#      ______     ____      ______     __     __                ______   __        __            ''''''
#    / _____/    / __ \    / _____\   |  |   / /              / _____/   \ \      / /          ''''''''''
#    \ \____    | /  \ |  | /         |  |__/ /     _____     \ \____     \ \    / /          ''@@''''''@@
#     \____ \   | |  | |  | |     __  |   __ \     |_____|     \____ \     \ \  / /           '''@@'''@@''
#    _____/ /   | \__/ |  | \____/ /  |  |  \ \               _____/ /      \ \/ /             ''''@@@'''
#    \_____/     \____/    \______/   |__|   \_\              \_____/        \__/                ''''''
class Server_API():
    def __init__(self):
        conf = Config()
        self.Master = []
        self.Users = []
        try:
            self.ServersConfig = conf.Get_Config()
        except:
            conf.Create_Config()
            self.ServersConfig = conf.Get_Config()

    def Server_Start(self,ola,a):
        Host = self.ServersConfig['Socket_Host']
        Port = self.ServersConfig['Socket_Port']
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((Host, int(Port)))
        s.listen(20)
        while True:
            conn, addr = s.accept()
            try:
                Thread(target=self.Clients_Socket, args=(conn, addr)).start()
            except:
                print('Thread dint start')
            # traceback.print_exc()

    def Clients_Socket(self, conn, addr):
        ip = str(addr).replace('(', '').replace(')', '').replace("'", "").split(',')[0]
        user1 = ''
        db = ''
        ha = Hash()
        fun = Fun()
        while True:
            #try:
                data = conn.recv(4096).decode()
                if data != '':
                    if self.ServersConfig['Socket_Encrypt'] == 'True':
                        trychack = ha.chacker(data)
                        if conn in self.Master:
                            gcmd = fun.Gobla_commands(data)
                            if gcmd != False:
                                if self.ServersConfig['Socket_Encrypt'] == 'True':
                                    ha.hashing(data)
                                conn.sendall(str(gcmd).encode())
                        elif conn in self.Users:
                            #print(data)
                            gcmd = fun.Gobla_commands(data, True, user1, True)
                            #print(gcmd)
                            if gcmd != False:
                                conn.sendall(str(gcmd).encode())
                        #print(trychack)
                        if trychack != False:
                            print(data)
                            data = trychack
                            print(data)
                            #print(str(data).split(' ')[0].lower() == 'login')
                            #print(str(len(self.Master)))
                            if str(data).split(' ')[0].lower() == 'login':
                                if self.ServersConfig['Enabel_Prem_Socket'] == 'False':
                                    if self.ServersConfig['Socket_Max_User'] <= str(len(self.Master)):
                                        conn.close()
                                    else:
                                        #try:
                                        user = str(data).split(' ')[1]
                                        pwd = str(data).split(' ')[2]
                                        #print(user)
                                        #print(pwd)
                                        test = self.Socket_Mater_Login_Fun(user, pwd)
                                        #print(test)
                                        if test:
                                            user1 = user
                                            self.Master.append(conn)
                                            conn.sendall('loged'.encode())
                                        else:
                                            conn.sendall('[phpMyAdmin2.0] User Or Passowrd WRONG'.encode())
                                            token = ''
                                            conn.close()
                                        #except:
                                        #    conn.sendall('[phpMyAdmin2.0] Login <user> <password>'.encode())
                                        #    conn.close()
                                else:
                                    try:
                                        user = str(data).split(' ')[1]
                                        pwd = str(data).split(' ')[2]
                                        test = self.Socket_Mater_Login_Fun(user, pwd)
                                        test2 = self.Socket_User_Login_Fun(user, pwd)
                                        print(user)
                                        print(pwd)
                                        if test:
                                            user1 = user
                                            self.Master.append(conn)
                                            conn.sendall('loged'.encode())
                                        elif test2:
                                            user1 = user
                                            self.Users.append(conn)
                                            conn.sendall('loged'.encode())
                                        else:
                                            conn.sendall('[phpMyAdmin2.0] User Or Passowrd WRONG'.encode())
                                            conn.close()
                                    except:
                                        conn.sendall('[phpMyAdmin2.0] Login <user> <password>'.encode())
                                        conn.close()
                            else:
                                conn.sendall('[phpMyAdmin2.0] Login <user> <password>'.encode())
                                conn.close()
                        else:
                            #print('ola')
                            conn.sendall('send_Encode_Plz'.encode())
                            pass
            #except:
            #    pass

    #  ______   __     _    __     __
    # |  ____| | |    | |  |  \   |  |
    # |  |__   | |    | |  | |\\  |  |
    # |   __|  | |    | |  | | \\ |  |
    # |  |     |  \__/ /   | |  \\|  |
    # |__|      \_____/    |_|   \___|
    def Socket_Mater_Login_Fun(self, user, pwd):
        MasterToken = self.ServersConfig['Maste_Token']
        MasterPassowrd = self.ServersConfig['Maste_Passowrd']
        print(user == MasterToken and pwd == MasterPassowrd)
        if user == MasterToken and pwd == MasterPassowrd:
            return True
        else:
            return False
    def Socket_User_Login_Fun(self,user,pwd):
        conf = Config()
        alluser = conf.Get_All_Users()
        #print(alluser)
        temp = []
        for i in alluser:
            temp.append(str(i).replace('.json',''))
        if user in temp:
            prems = conf.Get_User_Premes(user)
            #print(prems)
            allprems = str(prems).split(';')
            if 'socket.dbs.login' in allprems:
                pwdog = conf.Get_User_And_Passowrd(user)
                if pwd == pwdog:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False