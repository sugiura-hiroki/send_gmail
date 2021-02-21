# coding:utf8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from getpass import getpass
import time
jp = 'iso-2022-jp'

class Send_Gmail():
    def __init__(self, email_from, password=None):
        self.__email_from = email_from
        if type(password) == type(None):
            password = getpass('your password: ')
        self.__password = password

    def connect(self):
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        _ = smtpObj.login(self.__email_from, self.__password)
        return smtpObj

    def reconnect(func):
        def wrapper(self, *args, **kwargs):
            self.smtpOjb = self.connect()
            try:
                result = func(self, *args, **kwargs)
                self.smtpOjb.close()
                return result
            except Exception as exception:
                self.smtpOjb.close()
                raise exception
        return wrapper

    @property
    def email_from(self):
        return self.__email_from

    @reconnect
    def send(self, title, text, email_to):
        message = MIMEText(text.encode(jp), 'plain', jp)
        message['Subject'] = str(Header(title, jp))
        message['From'] = self.__email_from
        message['To'] = email_to
        self.smtpOjb.sendmail(
            self.__email_from,
            [email_to],
            message.as_string(),
        )

# def send_mail_stable(title, mail_txt):
#     for i in range(100):
#         try:
#             send_by_gmail(title, mail_txt)
#             break
#         except:
#             time.sleep(1)
#     else:
#         import pdb; pdb.set_trace()
