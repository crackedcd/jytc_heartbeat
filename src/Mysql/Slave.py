'''
Created on 2017年11月20日

@author: Administrator
'''

from multiprocessing.dummy import Pool as ThreadPool
import MySQLdb
from Notice.Notice import Notice

class Slave(object):
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
            conn = MySQLdb.connect(host=ip_addr, port=port, user="root", passwd="jytc$123")
            cursor = conn.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("show slave status")
            result = cursor.fetchone()
            if result["Slave_IO_Running"] != "Yes":
                msg = "{0}: [{1}->{2}]{3}".format("slave IO error", ip_addr, port, "从库断开连接!")
            if result["Slave_SQL_Running"] != "Yes":
                msg = "{0}: [{1}->{2}]{3}".format("slave SQL error", ip_addr, port, "从库断开连接!")
            conn.close()
        except Exception as e:
            msg = "{0}: [{1}->{2}]{3}".format(e, ip_addr, port, "探测失败!")
        finally:
            if msg:
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
        