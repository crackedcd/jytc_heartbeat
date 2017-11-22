'''
Created on 2017年11月20日

@author: Administrator
'''

from multiprocessing.dummy import Pool as ThreadPool
import MySQLdb
from Notice.Notice import Notice

class Mysql(object):
    '''
    classdocs
    '''

    def __init__(self, servers):
        '''
        Constructor
        '''
        self.servers = servers
        self.pool = ThreadPool(20)
    
    def __spy__(self, ip_addr, port = 3306):
        try:
            conn = MySQLdb.connect(host=ip_addr, port=port, user="root", passwd="")
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            cursor.fetchone()
            conn.close()
        except Exception as e:
            msg = "{0}: [{1}->{2}]{3}".format(e, ip_addr, port, "探测失败!")
            print(msg)
            n = Notice(msg)
            n.notice()
         
    def alive(self):
        for server in self.servers:
            for ip_addr in server:
                port = server[ip_addr]
#                 print(ip_addr)
#                 print(port)
                self.pool.apply_async(self.__spy__, args = (ip_addr, port))
        self.pool.close()
        self.pool.join()
