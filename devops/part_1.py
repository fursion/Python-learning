import psutil
import requests
import json
import Fursion.NotifyService
from Fursion.NotifyService import NotifyServiceParames, NotifyServiceMessageBody

Fursion.NotifyService.Host = 'http://localhost:5078'
Fursion.NotifyService.PushNotify(
    service='Mail', subject='测试', msg_type='html', to='604357968@qq.com', nickname='测试平台', body=NotifyServiceMessageBody({'code': '346768', 'timespan': '20'}))
