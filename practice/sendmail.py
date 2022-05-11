import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "zabbix@fursion.cn"
receiver = ["fursion@fursion.cn"]
mail_host = 'smtp.qiye.aliyun.com'
mail_user = 'zabbix@fursion.cn'
mail_pass = 'Dj970619'
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')  # 发送者
message['To'] = Header(receiver, 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL('smtp.qiye.aliyun.com', 465)
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
