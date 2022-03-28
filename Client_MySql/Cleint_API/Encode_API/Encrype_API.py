import hashlib
from API.DB_API import DB
class Hash():
    def __init__(self):
        self.hash_db = DB_hash()
        self.hash_db.create_DB()
    def hashing(self,msg):
        #print(self.hash_db.check_if_msg_register(msg))
        if self.hash_db.check_if_msg_register(msg) == []:
            hash_msg = hashlib.sha224(str(msg).encode()).hexdigest()
            #print(msg)
            #print(hash_msg)
            self.hash_db.add_msg_hash(str(msg),str(hash_msg))
            return hash_msg
    def chacker(self,hash):
        all = self.hash_db.get_hash_info()
        try:
            for i in all:
                if i[2] == hash:
                    return i[1]
            return False
        except:
            return False
    def check_code_register(self,msg):
        test = self.hash_db.check_if_msg_register(msg)
        if test == '[DB_API] ERROR DB NOT FOUND!!!':
            return False
        else:
            return True
class DB_hash():
    def __init__(self):
        self.db = DB()
    def create_DB(self):
        self.db.addDB('db_hash')
        self.db.addTabel('db_hash','hashs','de_hashed text,hashed text')
    def add_msg_hash(self,msg,hash):
        self.db.addinfotoTabel('db_hash','hashs',"'"+str(msg)+"','"+str(hash)+"'")
    def get_hash_info(self):
        return self.db.getInfo('db_hash','hashs')
    def check_if_msg_register(self,msg):
        return self.db.getInfo('db_hash','hashs','de_hashed',str(msg))