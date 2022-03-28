from API.DB_API import DB
from Configs.Config import Config
from Ferramentas.Export_Import import Tokens_Ex_In

class Fun():
    tks = Tokens_Ex_In()
    dbs = DB()
    conf = Config()
    def Convert_Commands_To_Premission(self,data,fromsocke=False,websocket=False):
        pem = ''
        if str(data).split(' ')[0].lower() == 'adddb':
            pem = 'dbs.addDB'
        elif str(data).split(' ')[0].lower() == 'rename':
            pem = 'dbs.rename'
        elif str(data).split(' ')[0].lower() == 'Rename_Tabel':
            pem = 'dbs.rename_tabel'
        elif str(data).split(' ')[0].lower() == 'deletedb':
            pem = 'dbs.deldb'
        elif str(data).split(' ')[0].lower() == 'addtable':
            pem = 'dbs.add_tabel'
        elif str(data).split(' ')[0].lower() == 'addinfototable':
            pem = 'dbs.add_info'
        elif str(data).split(' ')[0].lower() == 'getdata':
            pem = 'dbs.get_info'
        elif str(data).split(' ')[0].lower() == 'export':
            pem = 'dbs.export'
        elif str(data).split(' ')[0].lower() == 'import':
            pem = 'dbs.import'
        elif str(data).split(' ')[0].lower() == 'gettables':
            pem = 'dbs.get_tabels'
        elif str(data).split(' ')[0].lower() == 'removeinfo':
            pem = 'dbs.remove_info'
        else:
            return False
        if fromsocke == True:
            pem = 'socket.' + pem
        elif websocket == True:
            pem = 'websocket.' + pem
        return pem
    def Premission_Check(self,data,user,fromsocke=False,websocket = False):
        prims = self.conf.Get_User_Premes(user)
        pem = self.Convert_Commands_To_Premission(data,fromsocke,websocket)
        #print(prims)
        #print(pem)
        if pem != False:

            for i in str(prims).split(';'):
                #print(pem)
                #print(i)
                if i == '':
                    pass
                if str(i).split('.')[0]+'.'+str(i).split('.')[1]+'.'+str(i).split('.')[2] == pem:
                    try:
                        db_Name = str(i).split('.')[3]
                        if str(data).split(' ')[1] == db_Name:
                            try:
                                tb_Name = str(i).split('.')[4]
                                if str(data).split(' ')[2] == tb_Name:
                                    return True
                                else:
                                    return False
                            except:
                                return True
                        else:
                            return False
                    except:
                        return True
            return False
    def Gobla_commands(self,data,Prems = False,user = '',fromsocke=False,websocket=False):
        self.dbs = DB()
        if Prems == False:
            #Adicionar uma nova base de dados
            if str(data).split(' ')[0].lower() == 'adddb':
                try:
                    db = str(data).split(' ')[1].lower()
                    self.dbs.addDB(str(db))
                    return str(
                        '[MyAdmin2.0] DB ' + str(db) + ' Use Add successfully')
                except:
                    return str('[MyAdmin2.0-Error] Use AddDB <DB_Name>')
                    pass
            #Adicionar uma nova tabela
            elif str(data).split(' ')[0].lower() == 'addtable':
                try:
                    db = str(data).split(' ')[1].lower()
                    tb = str(data).split(' ')[2].lower()
                    contador = 0
                    sqlvars = ''
                    for i in str(data).split(' '):
                        if contador > 2:
                            if contador == 3:
                                sqlvars += i
                            else:
                                sqlvars += ' ' + i
                        contador += 1
                    test = self.dbs.addTabel(str(db), str(tb), str(sqlvars))
                    return test
                except:
                    return str('[MyAdmin2.0-Error] Use AddTable <DB_Name> <TB_Name> <SQL_Vars>')
                    pass
            # Adicionar infromacao a uma tabela
            elif str(data).split(' ')[0].lower() == 'addinfototable':
                try:
                    db = str(data).split(' ')[1].lower()
                    tabel = str(data).split(' ')[2].lower()
                    values = str(data).split(' ')[3].lower()
                    test = self.dbs.addinfotoTabel(db, tabel, values)
                    return str(test)
                except:
                    return str('[MyAdmin2.0-Error] Use AddInfoToTable <DB_Name> <TB_Name> <vars>')
                    pass
            # Pegar dados
            elif str(data).split(' ')[0].lower() == 'getdata':
                try:
                    db = str(data).split(' ')[1].lower()
                    tabel = str(data).split(' ')[2].lower()
                    try:
                        col = str(data).split(' ')[3].lower()
                        vars = str(data).split(' ')[4].lower()
                        test = self.dbs.getInfo(db, tabel, col, vars)
                        return str(test)
                    except:
                        test = self.dbs.getInfo(db, tabel)
                        return str(test)
                except:
                    return str(
                        '[MyAdmin2.0-Error] Use GetData <DB_Name> <TB_Name> ou Use GetData <DB_Name> <TB_Name> <Colune> <Vars>')
                    pass
            # Pegar tabelas
            elif str(data).split(' ')[0].lower() == 'gettables':
                try:
                    db = str(data).split(' ')[1].lower()
                    test = self.dbs.getTables(db)
                    return str(test)
                except:
                    return str('[MyAdmin2.0-Error] Use GetTables <DB_Name>')
                    pass
            # Mudar o Nome
            elif str(data).split(' ')[0].lower() == 'rename':
                try:
                    db_old = str(data).split(' ')[1].lower()
                    db_new = str(data).split(' ')[2].lower()
                    print(db_new)
                    print(str(data).split(' ')[2].lower())
                    TryDel = self.dbs.Rename_DB(db_old,db_new)
                    if TryDel == False:
                        return str(
                            '[MyAdmin2.0-Error] DB ' + str(db_old) + ' not found!!')
                    else:
                        self.dbs = DB()
                        return str(
                            '[MyAdmin2.0] DB ' + str(db_old) + ' Rename to ' + str(db_new))
                except:
                    return str(
                        '[MyAdmin2.0-Error] Use Rename <DB_OLD_Name> <DB_New_Name>')
                    pass
            #Export DB
            elif str(data).split(' ')[0].lower() == 'export':
                try:
                    FileName = str(data).split(' ')[1].lower()
                    TryExport = self.tks.add_Token(FileName)
                    if TryExport == False:
                        return str(
                            '[MyAdmin2.0-Error] DB ' + str(FileName) + ' not found!!')
                    else:
                        return str(TryExport)
                except:
                    return str(
                        '[MyAdmin2.0-Error] Use Export <FileName>')
                    pass
            #Apagar uma Base De Dados
            elif str(data).split(' ')[0].lower() == 'deletedb':
                try:
                    db = str(data).split(' ')[1].lower()
                    TryDel = self.dbs.Delete_DB(db)
                    if TryDel == False:
                        return str(
                            '[MyAdmin2.0-Error] DB ' + str(db) + ' not found!!')
                    else:
                        return str(
                            '[MyAdmin2.0] DB ' + str(db) + ' Removed')
                except:
                    return str(
                        '[MyAdmin2.0-Error] Use DelDB <DB_Name>')
                    pass
            # Remover Info
            elif str(data).split(' ')[0].lower() == 'removeinfo':
                try:
                    db = str(data).split(' ')[1].lower()
                    tabel = str(data).split(' ')[2].lower()
                    try:
                        col = str(data).split(' ')[3].lower()
                        vars = str(data).split(' ')[4].lower()
                        test = self.dbs.RemoveInfo(db, tabel, col, vars)
                        return str(test)
                    except:
                        test = self.dbs.RemoveInfo(db, tabel)
                        return str(test)
                except:
                    return str(
                        '[MyAdmin2.0-Error] Use GetData <DB_Name> <TB_Name> ou Use GetData <DB_Name> <TB_Name> <Colune> <Vars>')
                    pass
            else:
                return False
        else:
            print('Check Prems ', self.Premission_Check(data,user,fromsocke,websocket))
            if self.Premission_Check(data,user,fromsocke,websocket):
                # Adicionar uma nova base de dados
                if str(data).split(' ')[0].lower() == 'adddb':
                    try:
                        db = str(data).split(' ')[1].lower()
                        self.dbs.addDB(str(db))
                    except:
                        return str('[MyAdmin2.0-Error] Use AddDB <DB_Name>')
                        pass
                # Adicionar uma nova tabela
                elif str(data).split(' ')[0].lower() == 'addtable':
                    try:
                        db = str(data).split(' ')[1].lower()
                        tb = str(data).split(' ')[2].lower()
                        contador = 0
                        sqlvars = ''
                        for i in str(data).split(' '):
                            if contador > 2:
                                if contador == 3:
                                    sqlvars += i
                                else:
                                    sqlvars += ' '+i
                            contador += 1
                        test = self.dbs.addTabel(str(db), str(tb), str(sqlvars))
                        return test
                    except:
                        return str('[MyAdmin2.0-Error] Use AddTable <DB_Name> <TB_Name> <SQL_Vars>')
                        pass
                # Adicionar infromacao a uma tabela
                elif str(data).split(' ')[0].lower() == 'addinfototable':
                    try:
                        db = str(data).split(' ')[1].lower()
                        tabel = str(data).split(' ')[2].lower()
                        values = str(data).split(' ')[3].lower()
                        test = self.dbs.addinfotoTabel(db, tabel, values)
                        return str(test)
                    except:
                        return str('[MyAdmin2.0-Error] Use AddInfoToTable <DB_Name> <TB_Name> <vars>')
                        pass
                # Alterar tabela
                elif str(data).split(' ')[0].lower() == 'Alet_Var_Type':
                    try:
                        db = str(data).split(' ')[1].lower()
                        tabel = str(data).split(' ')[2].lower()
                        try:
                            col = str(data).split(' ')[3].lower()
                            vars = str(data).split(' ')[4].lower()
                            test = self.dbs.Alet_Var_Type(db, tabel, col, vars)
                            return str(test)
                        except:
                            return False
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use GetData <DB_Name> <TB_Name> ou Use GetData <DB_Name> <TB_Name> <Colune> <Vars>')
                        pass
                # Pegar dados
                elif str(data).split(' ')[0].lower() == 'getdata':
                    try:
                        db = str(data).split(' ')[1].lower()
                        tabel = str(data).split(' ')[2].lower()
                        try:
                            col = str(data).split(' ')[3].lower()
                            vars = str(data).split(' ')[4].lower()
                            test = self.dbs.getInfo(db, tabel, col, vars)
                            return str(test)
                        except:
                            test = self.dbs.getInfo(db, tabel)
                            return str(test)
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use GetData <DB_Name> <TB_Name> ou Use GetData <DB_Name> <TB_Name> <Colune> <Vars>')
                        pass
                # Export DB
                elif str(data).split(' ')[0].lower() == 'export':
                    try:
                        FileName = str(data).split(' ')[1].lower()
                        TryExport = self.tks.add_Token(FileName)
                        print(TryExport)
                        if TryExport == False:
                            return str(
                                '[MyAdmin2.0-Error] DB ' + str(FileName) + ' not found!!')
                        else:
                            return str(TryExport)
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use Export <FileName>')
                        pass
                #Import DB
                elif str(data).split(' ')[0].lower() == 'import':
                    try:
                        FileName = str(data).split(' ')[1].lower()
                        TryExport = self.tks.add_Token(FileName,'Import')
                        print(TryExport)
                        if TryExport == False:
                            return str(
                                '[MyAdmin2.0-Error] DB ' + str(FileName) + ' not found!!')
                        else:
                            return str(TryExport)
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use Export <FileName>')
                        pass
                #Pegar tabelas
                elif str(data).split(' ')[0].lower() == 'gettables':
                    try:
                        db = str(data).split(' ')[1].lower()
                        test = self.dbs.getTables(db)
                        return str(test)
                    except:
                        return str('[MyAdmin2.0-Error] Use GetTables <DB_Name>')
                        pass
                #Rename Tabel
                elif str(data).split(' ')[0].lower() == 'rename_tabel':
                    try:
                        db = str(data).split(' ')[1].lower()
                        Tabel_old = str(data).split(' ')[2].lower()
                        Tabel_new = str(data).split(' ')[3].lower()
                        TryDel = self.dbs.Rename_Tabel(db, Tabel_old,Tabel_new)
                        if TryDel == False:
                            return str(
                                '[MyAdmin2.0-Error] DB ' + str(db) + ' not found!!')
                        else:
                            dbs = DB()
                            return str(
                                '[MyAdmin2.0] DB ' + str(db) + 'Tabel '+str(Tabel_old)+' Rename to ' + str(Tabel_new))
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use Rename_Tabel <DB> <Tabal_Name> <New_Tabel_Name>'
                        )
                        pass
                # Mudar o Nome
                elif str(data).split(' ')[0].lower() == 'rename':
                    try:
                        db_old = str(data).split(' ')[1].lower()
                        db_new = str(data).split(' ')[2].lower()
                        TryDel = self.dbs.Rename_DB(db_old, db_new)
                        if TryDel == False:
                            return str(
                                '[MyAdmin2.0-Error] DB ' + str(db_old) + ' not found!!')
                        else:
                            dbs = DB()
                            return str(
                                '[MyAdmin2.0] DB ' + str(db_old) + ' Rename to ' + str(db_new))
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use Rename <DB_OLD_Name> <DB_New_Name>')
                        pass
                # Apagar uma tabela
                elif str(data).split(' ')[0].lower() == 'del_Tabel':
                    #try:
                    db = str(data).split(' ')[1].lower()
                    tb = str(data).split(' ')[2].lower()
                    try_del_db = self.dbs.del_Tabel(db,tb)
                    if try_del_db == False:
                        return str('[MyAdmin2.0-Error] Tabel '+str(tb)+' not Found')
                    elif try_del_db == True:
                        return str('[MyAdmin2.0] Tabel '+ str(tb) + ' Deleted')
                    else:
                        return str(
                            '[MyAdmin2.0-Error] DB ' + str(db) + ' not found!!')
                # Apagar uma Base De Dados
                elif str(data).split(' ')[0].lower() == 'deletedb':
                    #try:
                    db = str(data).split(' ')[1].lower()
                    TryDel = self.dbs.Delete_DB(db)
                    if TryDel == False:
                        return str(
                            '[MyAdmin2.0-Error] DB ' + str(db) + ' not found!!')
                    else:
                        return str(
                            '[MyAdmin2.0] DB ' + str(db) + ' Removed')
                    #except:
                    #    return str(
                    #        '[MyAdmin2.0-Error] Use DelDB <DB_Name>')
                    #    pass
                # Remover Info
                elif str(data).split(' ')[0].lower() == 'removeinfo':
                    try:
                        db = str(data).split(' ')[1].lower()
                        tabel = str(data).split(' ')[2].lower()
                        try:
                            col = str(data).split(' ')[3].lower()
                            vars = str(data).split(' ')[4].lower()
                            test = self.dbs.RemoveInfo(db, tabel, col, vars)
                            return str(test)
                        except:
                            test = self.dbs.RemoveInfo(db, tabel)
                            return str(test)
                    except:
                        return str(
                            '[MyAdmin2.0-Error] Use GetData <DB_Name> <TB_Name> ou Use GetData <DB_Name> <TB_Name> <Colune> <Vars>')
                        pass
                else:
                    return False
                #Done