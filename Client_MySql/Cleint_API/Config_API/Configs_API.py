import json
from os import walk
import os
class Config():
    def __init__(self):
        self.Paths = []
        self.Files = []
        self.loding_Config()
        print('Paths:',self.Paths)
        print('Files: ',self.Files)
    def Check_Config(self,filename,path):
        if path in self.Paths and '.\Config_API\Configs\ '.replace(' ','')+path+'\ '.replace(' ','')+filename in self.Files:
            return True
        return False
    def loding_Config(self):
        os.system('mkdir .\Config_API\Configs')
        for (dirpath, dirnames, filenames) in walk('.\Config_API\Configs'):
            if 'Configs' in str(dirpath).split('\ '.replace(' ','')):
                self.Paths.append(dirpath.replace('\ \ '.replace(' ',''),'\ ').replace(' ',''))
                print(str(dirpath))
        for i in self.Paths:
            for (dirpath, dirnames, filenames) in walk(str(i)):
                print(filenames)
                for a in filenames:
                    if 'json' in str(a).split('.'):
                        if str(i).replace(' ','\ '.replace(' ',''))+'\ '.replace(' ','')+a not in self.Files and dirpath == i:
                            self.Files.append(str(i).replace(' ','\ '.replace(' ',''))+'\ '.replace(' ','')+a)
    def add_Config(self,filename,info_js,Path=''):
        if Path != '' and '.\Config_API\Configs\ '.replace(' ','')+Path not in self.Paths:
            try:
                os.system('mkdir '+'.\Config_API\Configs\ '.replace(' ','')+Path)
            except:
                print('[Config_API] Error Creating Path ', '.\Config_API\Configs\ '.replace(' ','')+Path)
            config = open('.\Config_API\Configs\ '.replace(' ','')+Path+'\ '.replace(' ','') + filename + '.json', 'w')
            json.dump(info_js, config)
            return True
        else:
            config = open('.\Config_API\Configs\ '.replace(' ','')+filename+'.json','w')
            json.dump(info_js, config)
            return True
        return False

    def append_Config(self, filename, info_js, Path=''):
        if Path != '' and '.\Config_API\Configs\ '.replace(' ', '') + Path not in self.Paths:
            try:
                os.system('mkdir ' + '.\Config_API\Configs\ '.replace(' ', '') + Path)
            except:
                print('[Config_API] Error Creating Path ', '.\Config_API\Configs\ '.replace(' ', '') + Path)
            config = open('.\Config_API\Configs\ '.replace(' ', '') + Path + '\ '.replace(' ', '') + filename + '.json',
                          'a')
            json.dump(info_js, config)
            return True
        else:
            config = open('.\Config_API\Configs\ '.replace(' ', '') + filename + '.json', 'a')
            json.dump(info_js, config)
            return True
        return False
    def push_Config(self,filename,path=''):
        if path != '' and '.\Config_API\Configs\ '.replace(' ', '') + path  in self.Paths:
            config = open('.\Config_API\Configs\ '.replace(' ', '') + path + '\ '.replace(' ', '') + filename + '.json',
                          'r')
            return json.loads(config.read())
        else:
            config = open('.\Config_API\Configs\ '.replace(' ', '') + filename + '.json', 'r')
            return json.loads(config.read())