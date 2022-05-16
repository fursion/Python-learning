#!/usr/bin/python3
import argparse
import email.utils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sender", default='zabbix@fursion.cn', help="邮件发送者地址")
ap.add_argument('-sn', '--sender_nk', default='Zabbix', help="发件人昵称")
ap.add_argument('-S', "--Subject", default='', help="邮件主题")
ap.add_argument("-r", "--receiver", nargs='*', default=["fursion@fursion.cn"], help="收件人列表")
ap.add_argument('-t', '--Text',  help="文本信息")
ap.add_argument('-ht', '--HtmlText', help="Html超文本信息")
ap.add_argument('-u', '--user', default='zabbix@fursion.cn', help="用于登陆SMTP邮件服务器的用户名")
ap.add_argument('-sh', '--SMTP_HOST', default='smtp.qiye.aliyun.com', help="SMTP服务器地址")
ap.add_argument('-sp', '--SMTP_PW', default='2WZZVZ.qys487vz', help="SMTP登陆密码")
ap.add_argument('-R', '--reply_to', help="回信地址")
args = vars(ap.parse_args())
sender = args['sender']
receiver = args['receiver']
smtp_host = args['SMTP_HOST']
mail_user = args['user']
mail_pass = args['SMTP_PW']

message = MIMEMultipart('alternative')
message['Subject'] = Header(args['Subject'])
message['From'] = formataddr([args['sender_nk'], sender])
message['To'] = ",".join(receiver)  # 接收者
message['Reply-to'] = args['reply_to']
message['Message-id'] = email.utils.make_msgid()
message['Date'] = email.utils.formatdate()
if args['Text'] != '':
    text = MIMEText(args['Text'], _subtype='plain', _charset='UTF-8')
    message.attach(text)
elif args['HtmlText'] != '':
    htmltext = MIMEText(args['HtmlText'], _subtype='html', _charset='UTF-8')
    message.attach(htmltext)
try:
    smtpObj = smtplib.SMTP_SSL(smtp_host, 465)
    smtpObj.set_debuglevel(0)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPConnectError as e:
    print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
except smtplib.SMTPAuthenticationError as e:
    print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
except smtplib.SMTPSenderRefused as e:
    print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
except smtplib.SMTPRecipientsRefused as e:
    print('邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error)
except smtplib.SMTPDataError as e:
    print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
except smtplib.SMTPException as e:
    print('邮件发送失败, ', e.message)
except Exception as e:
    print('邮件发送异常, ', str(e))
