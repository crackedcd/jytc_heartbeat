'''
Created on 2017年11月20日

@author: Administrator
'''

from Notice.Mail import Mail
from Settings.Settings import Settings

class Notice(object):
    '''
    classdocs
    '''


    def __init__(self, content):
        '''
        Constructor
        '''
        l = Settings()
        self.maillist = l.get_maillist()
        self.content = content
        
    def notice(self):
        mail = Mail(self.maillist, self.content)
        mail.sendmail()
