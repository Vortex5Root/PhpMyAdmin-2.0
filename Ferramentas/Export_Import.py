from API.DB_API import DB
from secrets import *
class Tokens_Ex_In():
    def __init__(self):
        self.db = DB()
    def add_Token(self,file_Name,trypes = 'Export'):
        token = token_hex(16)
        self.db.addDB('Ex_In')
        self.db.addTabel('Ex_In',str(trypes),"link_Token text,file text")
        test = self.db.checkDB(file_Name)
        if test == True:
            self.db.addinfotoTabel('Ex_In',str(trypes),"'"+str(token)+"','"+str(file_Name)+"'")
            return '[MyAdmin2.0] http://127.0.0.1:5000/Fruntion/?Token=<Login_Encrypt_SHA256>&Ex_In='+token+' To '+str(trypes)+' '+file_Name
        return False
    def download_File(self,file_Name):
        self.db.RemoveInfo('Ex_In','Export','file',str(file_Name))
        return True
    def Import_File(self,file_Name):
        self.db.RemoveInfo('Ex_In','Import','file',str(file_Name))
        return True
    def Check_Token(self,token,trypes= 'Export'):
        #print('test',self.db.getInfo('Ex_In',str(trypes),'link_Token',str(token)))
        file = self.db.getInfo('Ex_In',str(trypes))
        print('all   ' ,file)
        for i in file:
            print('all ',i)
            if i[1] == token:
                return i[2]
        return False