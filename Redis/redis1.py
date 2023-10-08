import redis


class RedisFactory:
    'Redis实例工厂类'
    def CreateRedis(self):
        '创建新的Redis连接实例'
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return r


if __name__ == '__main__':

    r = RedisFactory().CreateRedis()
    da = r.json().get('PostContents:d4818ae5-52ed-459c-abe3-fd0ad5fd3f76')

    print(da)
