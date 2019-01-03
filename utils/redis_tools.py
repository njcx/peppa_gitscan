
import redis, datetime
import settings
from utils import logger

log = logger.logger(__name__)

class redistool(object):
    def __init__(self):
        try:
            pool = redis.ConnectionPool(host=settings.Redis_Host, password=settings.Redis_Pw, port=settings.Redis_Port, decode_responses=True)
            self.r = redis.Redis(connection_pool=pool)
        except Exception as e:
            print(e)
            log.error(e)

    def sadd(self, name, value):
        try:
            self.r.sadd(name, value)
        except Exception as e:
            print(e)
            log.error(e)


    def smembers(self, name):
        try:
            return self.r.smembers(name)
        except Exception as e:
            print(e)
            log.error(e)

    def scard(self, name):
        try:
            return self.r.scard(name)
        except Exception as e:
            print(e)
            log.error(e)

    def sismember(self, name, value):
        try:
            return self.r.sismember(name, value)
        except Exception as e:
            print(e)
            log.error(e)

    def spop(self, name):
        try:
            return self.r.spop(name)
        except Exception as e:
            print(e)
            log.error(e)

    def append_data(self, key, value):
        try:
            self.r.append(key, value)
        except Exception as e:
            print(e)
            log.error(e)

if __name__ == '__main__':
    try:
        nowTime = datetime.datetime.now().strftime('%Y/%m/%d')
        test = redistool()
        test.sadd(nowTime, 'test')
        print(test.scard(nowTime))
    except Exception as e:
        print(str(e))