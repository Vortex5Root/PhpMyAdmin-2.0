import sqlite3
import os
from os import walk

class DB():
    #                                            ____
    #   DDD  B$B$                  AAA          / __ \      |
    #   D  D $   $    ____        A   A        / /__\ \     |
    #   DDD  $$B$    |____|      AAAAAAA      /  ____  \    |
    #        B   $              A       A    /  /    \  \   |
    #        B$B$              A         A  /__/      \__\  |

    def __init__(self):
        self.dbs = []
        #try:
        os.system('mkdir .\API\DBS')
        #except:
        #    print('[DB_API] Dir DBS already exists')
        name = ''
        for (dirpath, dirnames, filenames) in walk('./API/DBS'):
            name = filenames
            break
        for i in name:
            if str(i).split('.')[1].lower() == 'db':
                self.dbs.append(str(i))
        #print(self.dbs)
    def checkDB(self,NameOFdb):
        for i in self.dbs:
            if str(NameOFdb).lower()+".db" == str(i):
                return True
        return False
    # ADD ***
    def addDB(self,NameOFdb):
        if str(NameOFdb) not in self.dbs:
            conn = sqlite3.connect('./API/DBS/'+str(NameOFdb).lower()+'.db')
            conn.commit()
            conn.close()
            return True
        else:
            return False
        #print('')
    def addTabel(self,NameOFdb,Nameoftabel,sqlvars):
        test = self.checkDB(NameOFdb)
        if test == True:
            conn = sqlite3.connect('./API/DBS/'+str(NameOFdb).lower()+'.db')
            c = conn.cursor()
            views = 0
            # Create uma tablea
            sqlcomd = "CREATE TABLE IF NOT EXISTS " + str(Nameoftabel)+"( ell text,"+sqlvars+")"
            c.execute(sqlcomd)
            conn.commit()
            conn.close()
            return True
        else:
            print('[DB_API] ERROR DB NOT FOUND!!!')
    def addinfotoTabel(self,NameOfdb,Nameoftabel,info):
        test = self.checkDB(NameOfdb)
        if test == True:
            Rows = self.getTablesRows(NameOfdb,Nameoftabel)
            #print(Rows)
            conn = sqlite3.connect('./API/DBS/' + str(NameOfdb).lower() + '.db')
            c = conn.cursor()
            sqlcmd = "INSERT INTO "+Nameoftabel+"("
            conta = 0
            for i in Rows:
                if conta == len(Rows)-1:
                    sqlcmd = sqlcmd + str(i)
                else:
                    sqlcmd = sqlcmd + str(i) + ","
                conta +=1
            sqlcmd = sqlcmd + ") VALUES ('All'," +info+");"
            #print(sqlcmd)
            c.execute(str(sqlcmd))
            conn.commit()
            conn.close()
        else:
            print('[DB_API] ERROR DB NOT FOUND!!!')
    #Get Row para facilitar o input de infromacao
    def getTablesRows(self,NameOfdb,Nameoftabel):
        test = self.checkDB(NameOfdb)
        if test == True:
            conn = sqlite3.connect('./API/DBS/' + str(NameOfdb).lower() + '.db')
            c = conn.cursor()
            sqlcomd = "SELECT * FROM "+str(Nameoftabel)
            Rows = c.execute(sqlcomd)
            names = list(map(lambda x: x[0], c.description))
            conn.commit()
            conn.close()
            return names
        else:
            print('[DB_API] ERROR DB NOT FOUND!!!')
    #Especial Get Info

    #Get Info
    def getInfo(self,NameOfdb,Nameoftabel,code = '',value = '',Expecial=''):
        test = self.checkDB(NameOfdb)
        info = ''
        if test == True:
            conn = sqlite3.connect('./API/DBS/' + str(NameOfdb).lower() + '.db')
            c = conn.cursor()
            if Expecial != '':
                sqlcomd = "SELECT "+str(Expecial)+" FROM "+str(Nameoftabel)
                info = c.execute(sqlcomd)
            elif value == '':
                sqlcomd = "SELECT * FROM "+str(Nameoftabel)+" WHERE ell = 'All'"
                info = c.execute(sqlcomd)
            elif code != '':
                sqlcomd = "SELECT * FROM " + str(Nameoftabel) + " WHERE " + str(code)
                info = c.execute(sqlcomd)
            else:
                sqlcomd = "SELECT * FROM "+str(Nameoftabel)+" WHERE "+str(code)+"  = '"+str(value)+"'"
                info = c.execute(sqlcomd)
            info = info.fetchall()
            conn.commit()
            conn.close()
            return info
        else:
            return '[DB_API] ERROR DB NOT FOUND!!!'
    #See All Tables
    def getTables(self,NameOfdb):
        DB = './API/DBS/'+NameOfdb+".db"
        try:
            con = sqlite3.connect(DB)
            cursor = con.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tabelas = cursor.fetchall()
            con.close()
            return tabelas
        except:
            return False
    #Get ALL DBS
    def getDBS(self):
        return self.dbs
    #Rename Db
    def Rename_DB(self,DB_OldName,DB_NewName):
        test = self.checkDB(DB_OldName)
        if test == True:
            os.rename(r'./API/DBS/'+DB_OldName+'.db',r'./API/DBS/'+DB_NewName+'.db')
            return True
        return False
    #Rename Tabel
    def Rename_Tabel(self,DB_Name,Old_Tabel_Name,New_Tabel_Name):
        test = self.checkDB(DB_Name)
        if test == True:
            try:
                sql = "RENAME TABLE " + str(Old_Tabel_Name) +' TO '+ str(New_Tabel_Name)+";"
                con = sqlite3.connect(DB_Name)
                cursor = con.cursor()
                cursor.execute(sql)
                con.commit()
                con.close()
                return True
            except:
                return False
    #dele
    def Alet_Var_Type(self,DB_Name,Tabel_Name,Clune_Name,now_type):
        test = self.checkDB(DB_Name)
        if test == True:
            try:
                sql = "ALTER TABLE "+str(Tabel_Name)+" ALTER COLUMN " + str(Clune_Name) +" "+str(now_type)+ ";"
                con = sqlite3.connect(DB_Name)
                cursor = con.cursor()
                cursor.execute(sql)
                con.commit()
                con.close()
                return True
            except:
                return False
        else:
            return 'db'
    #drop tabel
    def del_Tabel(self,NameOfdb,Tabel):
        test = self.checkDB(NameOfdb)
        if test == True:
            try:
                sql = "DROP TABLE "+str(Tabel)+";"
                con = sqlite3.connect(NameOfdb)
                cursor = con.cursor()
                cursor.execute(sql)
                con.commit()
                con.close()
                return True
            except:
                return False
        else:
            return 'db'
    #Del DB
    def Delete_DB(self,NameOfdb):
        test = self.checkDB(NameOfdb)
        print(test)
        if test == True:
            os.remove(r".\API\DBS"+r'\ '.replace(' ','')+str(NameOfdb)+'.db')
            return True
        return False
    #Remove
    def RemoveInfo(self,NameOfdb,NameOftabel,code = '',value = ''):
        test = self.checkDB(NameOfdb)
        info = ''
        if test == True:
            conn = sqlite3.connect('./API/DBS/' + str(NameOfdb).lower() + '.db')
            c = conn.cursor()
            if value == '':
                sqlcmd = "DELETE from "+str(NameOftabel)+" where * = *;"
                c.execute(sqlcmd)
            elif code != '' and value == '':
                sqlcmd = "DELETE from " + str(NameOftabel) + " where " + str(code) + "';"
                c.execute(sqlcmd)
            else:
                sqlcmd = "DELETE from " + str(NameOftabel) + " where "+str(code)+" = '"+str(value)+"';"
                c.execute(sqlcmd)
            conn.commit()
            conn.close()
            return True
        else:
            return False