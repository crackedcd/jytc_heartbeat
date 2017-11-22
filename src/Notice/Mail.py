'''
Created on 2017年11月20日

@author: Administrator
'''

from email.header import Header
from email.mime.text import MIMEText
import smtplib

class Mail(object):
    '''
    classdocs
    '''


    def __init__(self, maillist, content):
        '''
        Constructor
        '''
        self.maillist = maillist;
        self.content = content;
        self.smtp_server = '127.0.0.1'
        self.smtp_port = 25
        
    def sendmail(self):
        mail_addr = ", ".join(self.maillist)
        self.__send__(mail_addr, self.content)
            
        
    def __send__(self, mail_addr, content):
        try:
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['From'] = Header(u'JYTC')
            msg['To'] = Header(u'管理员 <%s>' % mail_addr)
            msg['Subject'] = Header(u'监控邮件', 'utf-8').encode()

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.set_debuglevel(1)
            server.sendmail('admin@jytc.com', mail_addr, msg.as_string())
            server.quit()
        except Exception as e:
            print("{0}: {1}, 内容为[{2}]".format("邮件发送失败", e, content))
