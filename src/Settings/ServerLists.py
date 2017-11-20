'''
Created on 2017年11月20日

@author: Administrator
'''

class ServerLists(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.servers = [
            {'127.0.0.1': 22},
            {'127.0.0.1': 222},
            {'111.75.156.107': 22},
            {'111.75.156.107': 222},
            {'117.42.112.108': 22},
            {'117.42.112.108': 222},
            {'220.176.108.80': 22},
            {'220.176.108.80': 222},
            {'117.42.75.42': 22},
            {'117.42.75.42': 222},
            ]

        self.mysqls = [
            {'127.0.0.1': 3306},
            {'127.0.0.1': 3307},
            {'127.0.0.1': 3308},
            ]

        self.mysqlslaves = [
            {'127.0.0.1': 3306},
            {'127.0.0.1': 3307},
            {'127.0.0.1': 3308},
            ]
        
        self.maillist = [
            "crackedcd@qq.com",
            "848@qq.com",
            ]
        
    def get_servers(self):
        return self.servers

    def get_mysqls(self):
        return self.mysqls
    
    def get_mysqlslaves(self):
        return self.mysqlslaves
    
    def get_maillist(self):
        return self.maillist
