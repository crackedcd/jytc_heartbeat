'''
Created on 2017年11月20日

@author: Administrator
'''

import pymysql
pymysql.install_as_MySQLdb()

from Settings.Settings import Settings
from Heartbeat.Server import Server
from Heartbeat.Mysql import Mysql
from Mysql.Slave import Slave


if __name__ == '__main__':
    l = Settings()
    servers = l.get_servers()
    mysqls = l.get_mysqls()
    mysqlslaves = l.get_mysqlslaves()
 
    s = Server(servers)
    s.alive()
     
    m = Mysql(mysqls)
    m.alive()
     
    slave = Slave(mysqlslaves)
    slave.alive()

