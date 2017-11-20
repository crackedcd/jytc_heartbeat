'''
Created on 2017年11月20日

@author: Administrator
'''

from multiprocessing.dummy import Pool as ThreadPool
import socket
from Notice.Notice import Notice


class Server(object):
    '''
    classdocs
    '''


    def __init__(self, servers):
        '''
        Constructor
        '''
        self.servers = servers
        self.pool = ThreadPool(20)
    
    def __socket__(self, ip_addr, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_result = sock.connect_ex((ip_addr, port))
        return sock_result
         
    def __spy__(self, ip_addr, port):
        err_code = self.__socket__(ip_addr, port)
        if 0 != err_code:
            msg = "{0}: [{1}->{2}]{3}".format(err_code, ip_addr, port, "探测失败!")
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
