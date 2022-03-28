from API.DB_API import DB

from Configs.Config import Config
from Ferramentas.function import Fun
import os
dbs = DB()
'''dbs = DB()
dbs.addDB('Computadores')
dbs.addTabel('Computadores','Portatais','CodigoProtatil int, Nome text, Categoria text')
print(dbs.getTablesRows('Computadores','Portatais'))
dbs.addinfotoTabel('Computadores','Portatais',"10,'veneno','24-11-2020'")
dbs.addinfotoTabel('Computadores','Portatais',"10,'ola','24-11-2020'")
dbs.addinfotoTabel('Computadores','Portatais',"10,'ad','23-11-2020'")
print(dbs.getInfo('Computadores','Portatais'))
print(dbs.getInfo('Computadores','Portatais','Categoria','24-11-2020'))'''
#                /\
#               @,.@
#              @,.,.@
#             @,.,.,.@
#            @,,.,.,,,@
#           @,.  /\   ,@
#          @,.  <££>  ,.@
#         @.,,.  \/  ,.,.@
#        @,.,.,,.,.,,,.,.,@
#       @,.,.,.,.,.,.,.,.,.@
#      /_@@@@@@@@@@@@@@@@@@_\
fun = Fun()
class cmd():
    def __init__(self):
        conf = Config()
        error = conf.Check_Users_Premes()
        print(error)
        lenofcmd = 40
        sv_conf = conf.Get_Config()
        while True:
            #     A     DDD   DDD
            #    A A    D  D  D  D   TTTTTTTT
            #   AAAAA   D  D  D  D      T      o P
            #  A     A  DDD   DDD       T
            os.system('clear')
            cmdsarry = ['######################', '#   PHP-MyAdmin 2.0  #', '######################', '\n']
            while True:
                os.system('clear')
                for i in cmdsarry:
                    print(i)
                cmd = input('>')
                ###########################
                #                         #
                #     Master_COMMANDS     #
                #                         #
                ###########################
                if len(cmdsarry) >= lenofcmd:
                    for an in range(len(cmdsarry)-lenofcmd):
                        cmdsarry.remove(cmdsarry[4])
                    cmdsarry.append('>' + str(cmd))
                else:
                    cmdsarry.append('>' + str(cmd))
                if str(cmd).split(' ')[0].lower() == 'clear' or str(cmd).split(' ')[0].lower() == 'cls':
                    break
                elif str(cmd).split(' ')[0].lower() == 'cmdsize':
                    try:
                        lenofcmd = int(str(cmd).split(' ')[1])
                        cmdsarry.append('[MyAdmin2.0] Cmd Size set ' + str(lenofcmd)) + ' successfully'
                    except:
                        cmdsarry.append('[MyAdmin2.0-Error] CmdSize Set ' + str(lenofcmd))
                elif str(cmd).split(' ')[0].lower() == 'adduser':
                    try:
                        user = str(cmd).split(' ')[1]
                        try:
                            perm = str(cmd).split(' ')[2]
                        except:
                            cmdsarry.append('[MyAdmin2.0-Error] Use AddUser '+str(user)+' <Perm>')
                        conf.add_User(user, perm)
                        cmdsarry.append('[MyAdmin2.0] User ' + str(user)+' add successfully')
                    except:
                        cmdsarry.append('[MyAdmin2.0-Error] Use AddUser <User> <Perm>')
                elif str(cmd).split(' ')[0].lower() == 'listuser':
                    #try:
                    alluser = conf.Get_All_Users()
                    stralluser = ''
                    for i in alluser:
                        if i == alluser[int(len(alluser)-1)]:
                            stralluser += str(i).replace('.json', '')
                        else:
                            stralluser += str(i).replace('.json','') + ' , '
                    cmdsarry.append('AllUseres: '+str(stralluser))
                    #except:
                    #    cmdsarry.append('[MyAdmin2.0-Error] Use listuser only'.encode())
                    #    pass
                elif str(cmd).split(' ')[0].lower() == 'removeuser':
                    try:
                        user = str(cmd).split(' ')[1]
                        try:
                            os.system('rm Useres/'+str(user)+'.json')
                            cmdsarry.append('[MyAdmin2.0] User ' + str(user) + ' Removed successfully')
                        except:
                            print('a')
                        try:
                            os.system('del /F Useres' +'\ '.replace(' ','')+ str(user) + '.json')
                            cmdsarry.append('[MyAdmin2.0] User ' + str(user) + ' Removed successfully')
                        except:
                            print('b')
                    except:
                        cmdsarry.append('[MyAdmin2.0-Error] Use RemoveUser <User>')
                ##############################
                #                            #
                #   SERVER-CONTROLER-Socket  #
                #                            #
                ##############################
                elif str(cmd).split(' ')[0].lower() == 'socket':
                    try:
                        args = str(cmd).split(' ')
                        args.remove(args[0])
                        ###################
                        #   Agrs Golbais  #
                        ###################
                        if(args[0] == '-h'):
                            cmdsarry.append(' _    _    _____    _        ____                ______     ____      ______     __     __                ______   __        __   ')
                            cmdsarry.append('| |  | |  |  ___|  | |      | __ \             / _____/    / __ \    / _____\   |  |   / /              / _____/   \ \      / /   ')
                            cmdsarry.append('| |__| |  | |__    | |      |  __/    _____    \ \____    | /  \ |  | /         |  |__/ /     _____     \ \____     \ \    / /    ')
                            cmdsarry.append('|  __  |  |  __|   | |      | |      |_____|    \____ \   | |  | |  | |     __  |   __ \     |_____|     \____ \     \ \  / /     ')
                            cmdsarry.append('| |  | |  | |___   | |__    | |                _____/ /   | \__/ |  | \____/ /  |  |  \ \               _____/ /      \ \/ /      ')
                            cmdsarry.append('|_|  |_|  |_____|  \____|   |_|                \_____/     \____/    \______/   |__|   \_\              \_____/        \__/       ')
                            cmdsarry.append('                                             ####################################                        ')
                            cmdsarry.append('                                             #           Sing_Command           #                        ')
                            cmdsarry.append('                                             ####################################                        ')
                            cmdsarry.append('                                             #  1-Socket -status                #                        ')
                            cmdsarry.append('                                             #  2-Socket -start                 #                        ')
                            cmdsarry.append('                                             #  3-Socket -stop                  #                        ')
                            cmdsarry.append('                                             #  4-Socket -info                  #                        ')
                            cmdsarry.append('                                             ####################################                        ')
                            cmdsarry.append('                                             #          Muilt_Commmds           #                        ')
                            cmdsarry.append('                                             ####################################                        ')
                            cmdsarry.append('                                             #  1-Socket -sethost <ip>          #                        ')
                            cmdsarry.append('                                             #  2-Socket -setPort <Port>        #                        ')
                            cmdsarry.append('                                             #                                  #                        ')
                            cmdsarry.append('                                             #                                  #                        ')
                            cmdsarry.append('                                             ####################################                        ')
                    except:
                        cmdsarry.append('[MyAdmin2.0-Error] Use socket -h to get HeLp!?')
                ##############
                #            #
                #    help    #
                ##############
                elif str(cmd).split(' ')[0].lower() == 'help':
                    cmdsarry.append(' _    _     _____   _        ____ ')
                    cmdsarry.append('| |  | |   /  ___| | |      / __ \ ')
                    cmdsarry.append('| |__| |  | |__    | |      |  __/ ')
                    cmdsarry.append('|  __  |  |  __|   | |      | /   ')
                    cmdsarry.append('| |  | |  | |___   | |__    | |   ')
                    cmdsarry.append('|_|  |_|  \_____|  \____|   |_|  ')
                    cmdsarry.append('')
                    cmdsarry.append('#################################')
                    cmdsarry.append('#         Master-Commands       #')
                    cmdsarry.append('#                               #')
                    cmdsarry.append('# 1-AddUser <User> <Perm>       #')
                    cmdsarry.append('# 2-AddUserPerm <User> <Perm>   #')
                    cmdsarry.append('# 3-RemoveUser <User>           #')
                    cmdsarry.append('# 4-InfoUser <User>             #')
                    cmdsarry.append('# 5-ListUseres                  #')
                    cmdsarry.append('# 6-CmdSize <Size>              #')
                    cmdsarry.append('# 7-Socket -h                   #')
                    cmdsarry.append('# 8-WebSocket -h                #')
                    cmdsarry.append('#                               #')
                    cmdsarry.append('##################################################')
                    cmdsarry.append('#                Commands/Prems                  #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('# 1-AddDB <DB_Name>                              #')
                    cmdsarry.append('#               (premes.dbs.add)                 #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('# 2-AddTabel <DB_Name> <TB_Name> <sqlvars>       #')
                    cmdsarry.append('#         (premes.dbs.add_tabel.<DBName>)        #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('# 3-AddInformation <DB_Name> <TB_Name> <valus>   #')
                    cmdsarry.append('#    (premes.dbs.addinfo.<DB_Name>.<TB_Name>)    #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('# 4-GetDate <DB_Name> <TB_Name>                  #')
                    cmdsarry.append('#    (premes.dbs.getdate.<DB_Name>.<TB_Name>)    #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('# 5-GetTabeles <DB_Name>                         #')
                    cmdsarry.append('#        (premes.dbs.gettabele.<DB_Name>)        #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('##################################################')
                    cmdsarry.append('#                   Teste-Server                 #')
                    cmdsarry.append('#                                                #')
                    cmdsarry.append('# 1-TestSocks <user> <passowrd>                  #')
                    cmdsarry.append('#              (Socket.dbs.login)                #')
                    cmdsarry.append('#              #Mor info Socks -p                #')
                    cmdsarry.append('# 2-TestWebSock <user> <passowrd>                #')
                    cmdsarry.append('# 3-TestPrems <user> <prem>                      #')
                    cmdsarry.append('##################################################')
                    if len(cmdsarry) >= lenofcmd:
                        for an in range(len(cmdsarry) - lenofcmd):
                            cmdsarry.remove(cmdsarry[4])
                else:
                    gcmd = fun.Gobla_commands(cmd)
                    if gcmd != False:
                        #if sv_conf['Socket_Encrypt'] == 'True':
                        #    ha.hashing(cmd)
                        cmdsarry.append(gcmd)
                    else:
                        cmdsarry.append('[MyAdmin2.0-Error] Type Help for help')
class Premicoes():
    def getPremisson(self,User,Prem):
        conf = Config()
        data = conf.getUserandPremes()
        print(data)
# Thread(target=).start()
# SAPI.Server_Start()