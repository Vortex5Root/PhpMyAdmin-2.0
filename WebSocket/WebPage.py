from multiprocessing import Process

import flask
from flask import request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
from Configs.Config import Config
from API.DB_API import DB
from Ferramentas.function import Fun
import os
from Socket.Socket_Encrype import Hash
from Ferramentas.Export_Import import Tokens_Ex_In
class Funtions():
    ex_in = Tokens_Ex_In()
    hash_killer = Hash()
    def __init__(self):
        conf = Config()
        try:
            self.ServersConfig = conf.Get_Config()
        except:
            conf.Create_Config()
            self.ServersConfig = conf.Get_Config()
    def WebAPI_Mater_Login_Fun(self,Token):
        data = self.hash_killer.chacker(Token)
        if data != False:
            user,pwd = data.split(' ')[1],data.split(' ')[2]
            MasterToken = self.ServersConfig['Maste_Token']
            MasterPassowrd = self.ServersConfig['Maste_Passowrd']
            #print(user == MasterToken and pwd == MasterPassowrd)
            if user == MasterToken and pwd == MasterPassowrd:
                return True
            else:
                return False
        else:
            return False
    def WebAPI_User_Login_Fun(self,Token):
        conf = Config()
        data = self.hash_killer.chacker(Token)
        if data != False:
            user, pwd = data.split(' ')[1], data.split(' ')[2]
            alluser = conf.Get_All_Users()
            # print(alluser)
            temp = []
            for i in alluser:
                temp.append(str(i).replace('.json', ''))
            if user in temp:
                prems = conf.Get_User_Premes(user)
                # print(prems)
                allprems = str(prems).split(';')
                if 'websocket.dbs.login' in allprems:
                    pwdog = conf.Get_User_And_Passowrd(user)
                    if pwd == pwdog:
                        return user
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

fun = Funtions()
cmd_global = Fun()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


def Export_File(user, token):
    conf = Config()
    alluser = conf.Get_All_Users()
    temp = []
    for i in alluser:
        temp.append(str(i).replace('.json', ''))
    if user in temp:
        prems = conf.Get_User_Premes(user)
        # print(prems)
        allprems = str(prems).split(';')
        if 'websocket.dbs.export' in allprems:
            filename = fun.ex_in.Check_Token(token)
            if filename != False:
                return filename
            return 'error'
    return False
def Import(user, token):
    conf = Config()
    alluser = conf.Get_All_Users()
    temp = []
    for i in alluser:
        temp.append(str(i).replace('.json', ''))
    if user in temp:
        prems = conf.Get_User_Premes(user)
        # print(prems)
        allprems = str(prems).split(';')
        if 'websocket.dbs.import' in allprems:
            filename = fun.ex_in.Check_Token(token,'Import')
            if filename != False:
                return filename
            return 'error'
    return False
@app.route('/Fruntion/',methods = ['GET','POST'])
def home():
    if 'Login' in request.args:
        md5pwd = str(request.args['Login'])
        check_1 = fun.WebAPI_User_Login_Fun(md5pwd)
        if fun.ServersConfig['Web_Master'] == 'True':
            check_2 = fun.WebAPI_User_Login_Fun(md5pwd)
            if check_1 == True or check_2 == True:
                return "Account Loged"
            else:
                return "Invalid: Login"
        elif check_1 == True:
            return "Account Loged"
        else:
            return "Invalid: Login"
    elif request.method == 'POST':
        #print(request.files)
        if 'files' in request.files:
            tk = request.form['Token']
            token = request.form['In']
            #print('Token:',tk)
            trylog = fun.WebAPI_User_Login_Fun(str(tk).replace(' ',''))
            if trylog != False:
                #print('loged')

                file_names = Import(str(trylog), token)
                try:
                    fun.ex_in.Import_File(file_names)
                    print('     Accertou missera ')
                except:
                    print('         error deliting the file')
                    # check if the post request has the file part
                if file_names != 'error':
                    #try:
                    if request.files:
                        f = request.files['files']
                        f.save(os.path.join('./API/DBS/',secure_filename(f.filename)))
                        db = DB()
                        return '''
                        
                        '''
                    #except:
                    #    print('error')
    elif 'Token' in request.args:
        if 'Fun' in request.args:
            md5pwd = str(request.args['Token'])
            check_1 = fun.WebAPI_User_Login_Fun(md5pwd)
            if fun.ServersConfig['Web_Master'] == 'True':
                check_2 = fun.WebAPI_User_Login_Fun(md5pwd)
                if check_1 == True:
                    command = str(request.args['Fun'])

                    cmd_global.Gobla_commands(cmd_global,True)
                elif check_2 == True:
                    command = str(request.args['Fun'])

                    cmd_global.Gobla_commands(cmd_global, False,)
                else:
                        return "Invalid: Login"
            elif check_1 == True:
                command = str(request.args['Fun'])
            else:
                return "Invalid: Login"
        elif 'In' in request.args:

            tk = request.args['Token']
            token = request.args['In']
            trylog = fun.WebAPI_User_Login_Fun(tk)
            if trylog != False:
                file_names = Import(str(trylog), token)
                if file_names != 'error':
                    return render_template('Import.html')
        elif 'Ex_In' in request.args:
            tk = request.args['Token']
            tk_Download = request.args['Ex_In']
            #print(tk_Download)
            trylog = fun.WebAPI_User_Login_Fun(tk)
            #print('TESTAAAAA    ',trylog)
            if trylog != False:
                #render_template('download.html')
                file_name= ''
                try:
                    file_name = Export_File(str(trylog),tk_Download)
                    try:
                        fun.ex_in.download_File(file_name)
                        print('     Accertou missera ')
                    except:
                        print('         error deliting the file')
                    if file_name != 'error':
                        return send_from_directory(r'..\API\DBS\ '.replace(' ', ''), filename=str(file_name) + '.db',
                                                   as_attachment=True)
                except:
                    pass
    else:
        return "Error: No id field provided. Please specify an id."
    #return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
app.debug=False
app.use_reloader=False
app.run()