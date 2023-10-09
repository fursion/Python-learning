import requests
import urllib
import json
Host = 'http://notify.service.fursion.cn'


class NotifyServiceMessageBody:
    '通知服务消息体,Data部分在调用信息模板时,为模板数据模型的Json序列化字符串'
    TemplateId: str
    Body: str
    Data: str

    def __init__(self, data=None, body: str = None, templateId: str = 'ad5ca306256945e4'):
        self.TemplateId = templateId
        self.Data = json.dumps(data)
        self.Body = body


class NotifyServiceParames:
    '通知服务调用参数'
    Service: str = 'Mail'
    Subject: str = 'Notify'
    msg_type: str = 'html'
    MessageBody: NotifyServiceMessageBody
    To: str
    NickName: str

    def __init__(self, service, subject, msg_type, to, body: NotifyServiceMessageBody, nickname='Notify'):
        self.Service = service
        self.Subject = subject
        self.msg_type = msg_type
        self.To = to
        self.MessageBody = body
        self.NickName = nickname


def Url():
    return urllib.parse.urljoin(Host, '/api/messages')


def Send(data: NotifyServiceParames):
    '发送推送请求'
    rep = requests.post(Url(), data=json.dumps(
        data, default=lambda o: o.__dict__, indent=4), headers={"Content-Type": "application/json"})
    if (rep.status_code == 200):
        print('调用推送服务成功 '+rep.text)
    else:
        print('调用推送服务失败 '+rep.text)


def PushNotify(service, subject, msg_type, to, body: NotifyServiceMessageBody, nickname='Notify'):
    '推送通知'
    data = NotifyServiceParames(
        service, subject, msg_type, to, body, nickname)
    Send(data)
