import os
from secrets import *
from os import walk
from Socket.Socket_Encrype import Hash
import json
#      _______     ____     __     __   _______    _    ______
#     / _____/    / __ \   |   \  | |  |  _____|  |_|  / _____/
#    | /         | /  \ |  |  \ \ | |  |  |__      _   \ \____
#    | |     __  | |  | |  |  |\ \| |  |   __|    | |   \____ \
#    | \____/ /  | \__/ |  |  | \ \ |  |  |       | |  _____/ /
#     \______/    \____/   |__|  \__|  |__|       |_|  \_____/
class Config():
    def __init__(self):
        self.ha =Hash()
        self.Users = []
        self.prems = []
        self.config_Servers = []
        self.Get_All_Users()
    ######################
    #    Servers-Config  #
    ######################
    def Create_Config(self):
        MasterToken = token_hex(64)
        MasterPassowrd = token_hex(64)
        config = {
            'Socket_Host': '127.0.0.1',
            'Socket_Port': '3316',
            'Socket_Encrypt': 'True',
            'Socket_Max_User': '1',
            'Enabel_Prem_Socket' : 'False',
            'Maste_Token': MasterToken,
            'Maste_Passowrd': MasterPassowrd,
            'Web_Host': '127.0.0.1',
            'Web_Port': '3317',
            'Web_Master' : 'False'
        }
        #print('New Config Created')
        self.ha.hashing('login ' + MasterToken + ' ' + MasterPassowrd)
        with open("config.json", "w") as f:
            json.dump(config, f)
    def Create_Premes_Register_Config(self):
        config = {
            'socket.dbs.login': 'False',
            'socket.dbs.addDB': 'False',
            'socket.dbs.add_tabel.*': 'False',
            'socket.dbs.add_info.*.*': 'False',
            'socket.dbs.rename': 'False',
            'socket.dbs.rename_tabel.*': 'False',
            'socket.dbs.get_tabels.*.': 'False',
            'socket.dbs.get_info.*.*' : 'False',
            'socket.dbs.Alet_Var_Type.*': 'False',
            'socket.dbs.deldb': 'False',
            'socket.dbs.del_Tabel': 'False',
            'socket.dbs.remove_info.*.*': 'False',
            'socket.dbs.import': 'False',
            'socket.dbs.export': 'False',
            'websocket.dbs.login': 'True',
            'websocket.dbs.rename': 'True',
            'websocket.dbs.rename_tabel.*': 'False',
            'websocket.dbs.addDB': 'True',
            'websocket.dbs.add_tabel.*': 'True',
            'websocket.dbs.add_info.*.*': 'True',
            'websocket.dbs.get_tabels.*': 'True',
            'websocket.dbs.get_info.*.*': 'True',
            'websocket.dbs.Alet_Var_Type.*': 'True',
            'websocket.dbs.deldb': 'False',
            'websocket.dbs.del_Tabel': 'False',
            'websocket.dbs.remove_info.*.*': 'True',
            'websocket.dbs.export': 'False',
            'websocket.dbs.import': 'False',
        }
        with open("Premes_Register_Config.json", "w") as f:
            json.dump(config, f)
    def Check_Premes_Register(self,prem):
        ile_name = "Premes_Register_Config.json"
        data = ''
        with open(ile_name) as f:
            data = json.load(f)
        if prem in data:
            return True
        return False
    ####################
    #      DeBuger     #
    ####################
    def Check_Users_Premes(self):
        alluser = self.Get_All_Users()
        error = []
        for i in alluser:
            #print(i)
            temppremes = self.Get_User_Premes(str(i).replace('.json',''))
            #print(temppremes)
            temppremes = str(temppremes).split(';')
            #print(temppremes)
            for a in temppremes:
                #print(a)
                if a != '':
                    tempa = str(a).split('.')[0] + '.' +str(a).split('.')[1] + '.' + str(a).split('.')[2]
                    s = ''
                    try:
                        s = str(a).split('.')[3]
                        s = '.*'
                        try:
                            s = str(a).split('.')[4]
                            s = '.*.*'
                        except:
                            tempa = tempa + s
                    except:
                        tempa = tempa + s
                    print(tempa)
                    if not self.Check_Premes_Register(tempa):
                        error.append('[Config_Error] the Premisson ' + str(a) + ' of User '+str(i)+' not FOUND in Register')
        if len(error) != 0:
            return error
    ####################
    #   Framentas-GET  #
    ####################
    def Get_Config(self):
        ile_name = "config.json"
        data = ''
        with open(ile_name) as f:
            data = json.load(f)
        if data not in self.config_Servers:
            self.config_Servers.append(data)
        else:
            return self.config_Servers
        return data
    def Get_All_Users(self):
        name = ''
        alluser = []
        for (dirpath, dirnames, filenames) in walk('./Useres'):
            name = filenames
            break
        for i in name:
            if str(i).split('.')[1].lower() == 'json':
                alluser.append(i)
                if i not in self.Users:
                    self.Users.append(str(i).replace('.json',''))
        return alluser
    def add_User(self, Username, Premes):
        passowrd = token_hex(64)
        try:
            os.system('mkdir Useres')
        except:
            print('[MyAdmin] Dir Useres already exists')
        config = {
            'User': str(Username),
            'Passowrd': str(passowrd),
            'Premissios': Premes
        }
        if 'socket.dbs.login' in str(Premes).split(';'):
            #print('test')
            self.ha.hashing('login ' + Username + ' ' + passowrd)
        with open("./Useres/"+str(Username)+".json", "a") as f:
            json.dump(config, f)
        return passowrd
    def Get_User_Premes(self,user):
        #print(self.Users)
        if str(user) in self.Users:
            try:
                os.system('mkdir Useres')
            except:
                print('[MyAdmin] Dir Useres already exists')

            ile_name = './Useres/'+str(user)+'.json'
            data = ''
            with open(ile_name) as f:
                data = json.load(f)
            if data not in self.prems:
                self.prems.append(data['Premissios'])
            #print(data)
            return data['Premissios']

    def Get_User_And_Passowrd(self,user):
        if user in self.Users:
            try:
                os.system('mkdir Useres')
            except:
                print('[MyAdmin] Dir Useres already exists')

            ile_name = './Useres/'+str(user)+".json"
            data = ''
            with open(ile_name) as f:
                data = json.load(f)
            if data not in self.prems:
                self.prems.append(data['Passowrd'])
            return data['Passowrd']